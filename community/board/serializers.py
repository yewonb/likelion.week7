from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields=['id', 'post', 'created_at', 'comment']
    read_only_fields=['post']

class PostDetailSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields=['id', 'title', 'body', 'created_at', 'comments']
