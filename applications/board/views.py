from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from applications.board.models import Post
from applications.board.serializer import PostSerializer
from applications.user.models import User
from argon2 import PasswordHasher


class PostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    게시글 생성 및 조회
    - 제목 최대 20자, 본문 최대 200자 제한
    - 제목 && 본문 이모지 포함 가능
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        print(int(str(self.queryset.reverse().first())) + 1)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        try:
            title = request.data['title']
            content = request.data['content']
            password = request.POST.get('password')

            if len(title) > 20:
                return Response("제목이 20자를 초과합니다.")
            elif len(content) > 200:
                return Response("본문이 200자를 초과합니다.")

            self.create(request)
            if password:
                user = User()
                user.post = self.queryset.reverse().first()
                # user.post = int(str(self.queryset.reverse().first())) + 1
                user.password = PasswordHasher().hash(password)
                user.save()
            return Response("성공적으로 생성되었습니다.")
        except Exception as e:
            print(e)
            return Response("게시글이 정상적으로 생성되지 않았습니다.")

class UserDetailMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    게시글 정보 수정 및 탈퇴
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # try:
        #     queryset = User.objects.select_related('password')
        return self.destroy(request, *args, **kwargs)

