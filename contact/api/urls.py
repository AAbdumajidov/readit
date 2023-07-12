from django.urls import path
from .views import PostListCreateAPIView


urlpatterns = [
    path('list-create/', PostListCreateAPIView.as_view())
]