from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

urlpatterns = [
    path("list/<str:data>", views.list.as_view(), name="List Methond"),
    path("manifest", views.Manifest.as_view(), name="Manifest"),
    path("payment", views.Payment.as_view(), name="Payment"),
]
