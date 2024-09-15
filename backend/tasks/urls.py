from django.urls import path
from .views import TaskListCreate, TaskDetail, RegisterView

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
