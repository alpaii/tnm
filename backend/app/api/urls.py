from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ItemViewSet,
    AccountViewSet,
    CategoryViewSet,
    CategoryDetailViewSet,
    TransactionViewSet,
    MonthlyViewSet,
)

router = DefaultRouter()
router.register(r"items", ItemViewSet, basename="item")
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"categorydetails", CategoryDetailViewSet, basename="categorydetail")
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"monthly", MonthlyViewSet, basename="monthly")

urlpatterns = router.urls
