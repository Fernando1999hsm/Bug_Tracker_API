from rest_framework import serializers
from .models import Issue, Application

class IssueSerializer(serializers.ModelSerializer):
    application = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = '__all__'


class IssueListSerializer(serializers.ModelSerializer):
    application = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = ['id', 'title', 'severity', 'status', 'application', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'code', 'name']