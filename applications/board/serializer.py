from applications.board.models import Post

from rest_framework import serializers

class PostModelSerializer(serializers.ModelSerializer):
    """
    게시글 serializer
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']