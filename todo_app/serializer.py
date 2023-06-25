from rest_framework import serializers
from todo_app.models import todo_model

class todo_serializer (serializers.ModelSerializer) :
    class Meta:
        model = todo_model
        fields = '__all__'
        