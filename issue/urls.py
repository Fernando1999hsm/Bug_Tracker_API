from django.urls import path
from . import views

urlpatterns = [
    path('issues/', views.IssueListView.as_view(), name='issue-list'),
    path('issues/<int:pk>/', views.IssueDetailView.as_view(), name='issue-detail'),
]
