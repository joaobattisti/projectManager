from django.urls import path
from .views import list_project, new_project, update_project, delete_project

urlpatterns = [
    path('list/', list_project, name="list_project"),
    path('new/', new_project, name="new_project"),
    path('update/<int:id>/', update_project, name="project_update"),
    path('delete/<int:id>/', delete_project, name="project_delete"),
]

