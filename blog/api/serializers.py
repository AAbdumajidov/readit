from rest_framework import serializers
from ..models import Category, Tag, Article, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticleGetSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.title', read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'description', 'category', 'tags', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'description', 'category', 'tags', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance
