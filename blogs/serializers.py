from rest_framework import serializers
from .models import BlogPost, Comment, UpvoteDownvote


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UpvoteDownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvoteDownvote
        fields = '__all__'
