from rest_framework import serializers

from blog.models import Post, Comment
from users.models import GeekUser


# HW8
class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = ("id", "email", "is_staff", "is_active", "date_joined")

class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = "__all__"
        fields = ("id", "name", "comment", "created", "post")
        # fields = ("name", "comment", "created")


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created", "cover", "category")


class PostDetailSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created", "status", "cover", "post_comment")


