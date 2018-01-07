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

    def validate(self, data):
        """
        Check that image or video have something.
        """
        image = data.get('image', None)
        video = data.get('video', None)
        if (image == '' or image == None) and  (video == '' or video == None):
            raise serializers.ValidationError("Image or video must be set.")
        return data