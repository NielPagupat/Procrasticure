from django.urls import path
from .views import createTimeTasksAPIView, getMyTaskListAPIView, CRUDTimeTaskAPIView
urlpatterns = [
    path('createTimedTask/', createTimeTasksAPIView.as_view(), name="create-timed tasks"),
    path('editTimeTask/<int:pk>', CRUDTimeTaskAPIView.as_view(), name="edit-time Task"),
    path('getTimedTaskHistory/<str:email>/', getMyTaskListAPIView.as_view(), name="get-task-List")
]
