from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import BlogPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    username_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'text', 'created', 'post', 'username_name']

    def get_username_name(self, obj):
        return obj.username.username


class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = BlogPost

        fields = ['id', 'title', 'author', 'content', 'rate', 'created', 'author_name', 'comment_set']

    def get_author_name(self, obj):
        return obj.author.username