from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    #Task crud serializer
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'created_at']
        read_only_fields = ['created_at']