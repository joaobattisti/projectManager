from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from projects import urls as projects_urls
from activities import urls as activities_urls
from home import urls as home_urls


urlpatterns = [
    path('', include(home_urls)),
    path('projects/', include(projects_urls)),
    path('activities/', include(activities_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
