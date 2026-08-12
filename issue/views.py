from django.db.models import Count, Q
from rest_framework import generics
from .models import Issue, Application
from .serializers import IssueSerializer, IssueListSerializer, ApplicationSerializer

class IssueListView(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueListSerializer

class IssueDetailView(generics.RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.annotate(
        open_issues_count=Count('issues', filter=Q(issues__status=True))
    )
    serializer_class = ApplicationSerializer
