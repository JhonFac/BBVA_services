from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

# router.register(r"payment", views.PaymentViewSet, basename="Payment"),
# router.register(r"manifest", views.ManifestViewSet, basename="Manifest"),
router.register(r"transactions", views.GenerateTransactionViewSet, basename="Transactions"),
# router.register(r"create_transaction", views.CreateTransactionViewSet, basename="Create transaction"),

urlpatterns = [
    path("get_transaction/<str:idOrder>/", views.GetTransaction.as_view(), name="Get transaction"),
    path("create_transaction/", views.CreateTransaction.as_view(), name="Create transaction"),
    path("manifest/", views.ManifestViewSet.as_view(), name="manifest"),
    path("payment-methods/", views.PaymentViewSet.as_view(), name="manifest"),
    path("", include(router.urls))
]
    