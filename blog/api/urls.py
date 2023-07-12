from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRUDView,
    TagListCreateAPIView,
    TagRUDView,
    ArticleListCreateAPIView,
    ArticleRUDAPIView,
    CommentListCreateAPIView,
    CommentRUDAPIView
)


urlpatterns = [
    path('category/list-create/', CategoryListCreateAPIView.as_view()),
    path('category/rud/<int:pk>/', CategoryRUDView.as_view()),
    path('tag/list-create/', TagListCreateAPIView.as_view()),
    path('tag/rud/<int:pk>/', TagRUDView.as_view()),
    path('article/list-create/', ArticleListCreateAPIView.as_view()),
    path('article/rud/<int:pk>/', ArticleRUDAPIView.as_view()),
    path('article/<int:article_id>/comment/list-create/', CommentListCreateAPIView.as_view()),
    path('comment/rud/<int:pk>/', CommentRUDAPIView.as_view()),
]