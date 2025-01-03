from rest_framework import viewsets # type: ignore
from .serializer import TaskSerializer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryser = Task.object.all()