from rest_framework import serializers

from posts.models import Post, Category
from users.serializers import UserSerializer


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','image', 'summary', 'publication_date']


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'