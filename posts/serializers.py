from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_post_id', 'comment_author', 'comment_content', 'comment_likes', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post_author', 'post_content', 'post_title', 'post_resume', 'post_likes', 'created_at', 'updated_at', 'comments']
