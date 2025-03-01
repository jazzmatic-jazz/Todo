from rest_framework.serializers import ModelSerializer
from api.models import Todo


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['user','created_at', 'title', 'description', 'status', 'due_date']