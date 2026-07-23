from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer, IssueListSerializer

class IssueListView(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueListSerializer

class IssueDetailView(generics.RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
