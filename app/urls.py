from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

urlpatterns = [
    path("list", views.list.as_view(), name="list"),

]
