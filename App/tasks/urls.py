from django.urls import path
from .views import createTaskAPIView, CRUDTaskAPIView, getMyTaskListAPIView

urlpatterns = [
    path("createTask/", createTaskAPIView.as_view(), name='create-project'),
    path("editTask/<int:pk>", CRUDTaskAPIView.as_view(), name='Edit-Task'),
    path('getmytask/<str:email>', getMyTaskListAPIView.as_view(), name="my-tasks"),
]
