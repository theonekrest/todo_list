from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name = 'task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task-detail'),
    path('create/', TaskCreate.as_view(), name = 'task-create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name= 'task-delete'),
    path('login/', TaskLogin.as_view(), name='task-login'),
    path('logout/', LogoutView.as_view(), name='task-logout')
]
