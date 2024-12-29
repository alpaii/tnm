from rest_framework import serializers
from .models import Item, Account, Category, CategoryDetail, Transaction, Monthly


# 테스트
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "name", "balance", "type"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested representation
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source="category"
    )

    class Meta:
        model = CategoryDetail
        fields = ["id", "category", "category_id", "name"]


class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)  # Nested representation
    account_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True, source="account"
    )

    category_detail = CategoryDetailSerializer(read_only=True)
    category_detail_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoryDetail.objects.all(), write_only=True, source="category_detail"
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "account",
            "account_id",
            "date",
            "amount",
            "name",
            "category_detail",
            "category_detail_id",
        ]


class MonthlySerializer(serializers.ModelSerializer):
    category_detail = CategoryDetailSerializer(read_only=True)
    category_detail_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoryDetail.objects.all(), write_only=True, source="category_detail"
    )

    class Meta:
        model = Monthly
        fields = ["id", "category_detail", "category_detail_id", "amount", "date"]
