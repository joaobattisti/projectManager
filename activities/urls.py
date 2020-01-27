from django.urls import path
from .views import list_activities, new_activity, update_activity, delete_activity

urlpatterns = [
    path('list/', list_activities, name="list_activities"),
    path('new/', new_activity, name="new_activity"),
    path('update/<int:id>/', update_activity, name="activity_update"),
    path('delete/<int:id>/', delete_activity, name="activity_delete"),
]

