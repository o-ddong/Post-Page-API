import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from applications.board.models import Post
from applications.board.serializer import PostSerializer
from django.core.paginator import Paginator
from argon2 import PasswordHasher
import re


class PostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    게시글 생성 및 조회
    - 제목 최대 20자, 본문 최대 200자 제한
    - 제목 && 본문 이모지 포함 가능
    """
    queryset = Post.objects.all().order_by("-id")
    page = Paginator(queryset, 20)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            title = data['title']
            content = data['content']
            password = data['password']

            if len(title) > 20:
                return Response("제목이 20자를 초과합니다.")
            elif len(content) > 200:
                return Response("본문이 200자를 초과합니다.")
            if not password_convertion(password):
                return Response("비밀번호 양식에 맞지 않습니다.")
            if len(password) < 6:
                return Response("비밀번호가 너무 짧습니다.")

            # weather = send_weather_api()

            return self.create(request)
        except Exception as e:
            print(e)
            return Response("게시글이 정상적으로 생성되지 않았습니다.")

class PostDetailDeleteMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    게시글 정보 수정 및 탈퇴
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, pk, *args, **kwargs):
        password = request.data['password']
        queryset = Post.objects.filter(id=pk, password=password)
        if not queryset:
            return Response("해당하는 게시물이 존재하지 않습니다.")
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        password = request.data['password']
        queryset = Post.objects.filter(id=pk, password=password)
        if not queryset:
            return Response("해당하는 게시물이 존재하지 않습니다.")
        return self.destroy(request, *args, **kwargs)


def password_convertion(pw):
    """ 패스워드 양식 체크 """
    result = re.compile('[0-9]')
    if len(result.findall(pw)) < 1:
        return False
    return True

def send_weather_api():
    URL = 'http://api.weatherapi.com/v1/current.json?key=189801d7b61741d797e135108220709&q=Korea&aqi=no'
    response = requests.get(URL)
    data = response.json()
    return data['current']['condition']['text']
