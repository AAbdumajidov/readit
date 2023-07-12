from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CategorySerializer, TagSerializer, ArticleGetSerializer, ArticlePostSerializer, CommentSerializer
from ..models import Category, Tag, Article, Comment
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly


# Category view
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


# Tag view
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# Article APIview
class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.order_by('-id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.queryset.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArticleRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


# Comment APIVIew
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permissions = [IsAdminUserOrReadOnly]



# 49:32


