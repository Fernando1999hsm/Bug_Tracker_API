from django.db.models import Count, Q
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Issue, Application
from .serializers import IssueSerializer, IssueListSerializer, ApplicationSerializer

class ReadOnlyMixin:
    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response(
            {'error': 'Solo se permiten peticiones GET.'},
            status=status.HTTP_200_OK
        )

class IssueListView(ReadOnlyMixin, generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueListSerializer

class IssueDetailView(ReadOnlyMixin, generics.RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ApplicationListView(ReadOnlyMixin, generics.ListAPIView):
    queryset = Application.objects.annotate(
        open_issues_count=Count('issues', filter=Q(issues__status=True))
    )
    serializer_class = ApplicationSerializer
