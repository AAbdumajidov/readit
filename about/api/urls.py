from django.urls import path
from .views import FeedbackListCreateAPIView, FeedbackRUDView


urlpatterns = [
    path('list-create/', FeedbackListCreateAPIView.as_view()),
    path('rud/<int:pk>', FeedbackRUDView.as_view()),
]