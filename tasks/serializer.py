from rest_framework import serializers
from .models import Task

class TastkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'tittle', 'description', 'done')
        fields = '__all__'