from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('tasks/', include('App.tasks.urls')),
    path('timedtasks/', include('App.productivity_tracker.urls')),
]