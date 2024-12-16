from django.shortcuts import render
from .serializers import createTask
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import task

# Create your views here.
class createTaskAPIView(ListCreateAPIView):
    serializer_class = createTask
    queryset = task.objects.all()

class CRUDTaskAPIView(RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = createTask

class getMyTaskListAPIView(ListAPIView):
    serializer_class = createTask
    def get_queryset(self):
        owner=self.kwargs['email']
        return task.objects.filter(task_owner=owner)


