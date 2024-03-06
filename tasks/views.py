from rest_framework import viewsets
from .serializer import TastkSerializer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TastkSerializer
    queryset = Task.objects.all()