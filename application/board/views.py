from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from application.board.models import Post
from application.board.serializer import PostSerializer


class PostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    게시글 생성 및 조회
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

