from django.shortcuts import render
from .serializers import createTaskTimer
from .models import productivityTimer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class createTimeTasksAPIView(ListCreateAPIView):
    serializer_class = createTaskTimer
    queryset = productivityTimer.objects.all()

class CRUDTimeTaskAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = createTaskTimer
    queryset = productivityTimer.objects.all()

class getMyTaskListAPIView(ListAPIView):
    serializer_class = createTaskTimer
    def get_queryset(self):
        owner=self.kwargs['email']
        return productivityTimer.objects.filter(owner=owner)

