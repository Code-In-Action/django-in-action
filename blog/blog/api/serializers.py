from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment, Category

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ['id', 'body', 'post', 'owner']



class CategorySerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
  class Meta:
    model = Category
    fields = ['id', 'name', 'owner', 'posts']
    
