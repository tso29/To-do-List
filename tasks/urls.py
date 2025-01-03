from django.urls import path, include # type: ignore
from rest_framework import routers # type: ignore
from tasks import views

# api versioning
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path("api/v1/", include(router.urls))
]

# Genera las rutas GET POST PUT DELETE