from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('todo', views.taskList, name="task-list"),
    path('todo/<str:pk>', views.taskDetail, name="task-Detail"),
    path('todo-update/<str:pk>', views.taskUpdate, name="task-update"),
    path('todo-create', views.taskCreate, name="task-Create"),
    path('todo-delete/<str:pk>', views.taskDelete, name="task-Delete"),
]