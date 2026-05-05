from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('create_project/', create_project, name="create_project"),
    path('project/<int:project_id>/', project_detail, name="project_detail"),
    path('create-task/<int:project_id>/', create_task, name="create_task"),
    path('update-task/<int:task_id>/', update_task, name="update_task"),
    path('project/<int:project_id>/members/', manage_members, name="manage_members"),
]