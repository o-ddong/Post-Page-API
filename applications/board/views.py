from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from applications.board.models import Post
from applications.board.serializer import PostModelSerializer


class PostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    게시글 생성 및 조회
    """
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request)
        except Exception as e:
            print(e)
            return Response("게시글이 생성되지 않았습니다.")



