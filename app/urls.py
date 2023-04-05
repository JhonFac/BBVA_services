from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

router.register(r"payment", views.PaymentViewSet, basename="Payment"),

urlpatterns = [
    path("list/", views.list.as_view(), name="List Methond"),
    path("get_transaction/<str:idOrder>", views.GetTransaction.as_view(), name="Get Transaction"),
    # path("payment", views.Payment.as_view(), name="Payment"),
    path("manifest", views.Manifest.as_view(), name="Manifest"),
    path("", include(router.urls)),
]
