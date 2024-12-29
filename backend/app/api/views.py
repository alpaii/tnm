from rest_framework.viewsets import ModelViewSet
from .models import Item, Account, Category, CategoryDetail, Transaction, Monthly
from .serializers import (
    ItemSerializer,
    AccountSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
    TransactionSerializer,
    MonthlySerializer,
)


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailViewSet(ModelViewSet):
    queryset = CategoryDetail.objects.all()
    serializer_class = CategoryDetailSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class MonthlyViewSet(ModelViewSet):
    queryset = Monthly.objects.all()
    serializer_class = MonthlySerializer
