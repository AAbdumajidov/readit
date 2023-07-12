from django.urls import path
from .views import index, article_list, article_detail

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('list/', article_list, name='list'),
    path('detail/<int:pk>/', article_detail, name='detail'),
]