from django.db.migrations import serializer
from application.board.models import Post


class PostSerializer(serializer.ModelSerializer):
    """
    게시글 serializer
    """
    class Meta:
        model = Post
        field = "__all__"