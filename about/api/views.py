from rest_framework import generics, permissions

from ..models import Feedback
from .serializers import FeedbackSerializer
from .permissions import IsAdminUserOrReadOnly


class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUserOrReadOnly]


