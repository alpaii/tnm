from django.test import TestCase
from api.models import Account, Category, CategoryDetail, Transaction, Monthly
from api.serializers import (
    AccountSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
    TransactionSerializer,
    MonthlySerializer,
)
from datetime import date
from django.utils.timezone import make_aware


class AccountSerializerTest(TestCase):
    def setUp(self):
        self.account_data = {
            "name": "Test Account",
            "balance": 2000,
            "type": "Bank",
        }
        self.account = Account.objects.create(**self.account_data)

    def test_account_serialization(self):
        serializer = AccountSerializer(self.account)
        self.assertEqual(serializer.data["name"], self.account_data["name"])
        self.assertEqual(serializer.data["balance"], self.account_data["balance"])
        self.assertEqual(serializer.data["type"], self.account_data["type"])

    def test_account_deserialization(self):
        serializer = AccountSerializer(data=self.account_data)
        self.assertTrue(serializer.is_valid())
        account = serializer.save()
        self.assertEqual(account.name, self.account_data["name"])


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")

    def test_category_serialization(self):
        serializer = CategorySerializer(self.category)
        self.assertEqual(serializer.data["name"], "Groceries")

    def test_category_deserialization(self):
        data = {"name": "Utilities"}
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())
        category = serializer.save()
        self.assertEqual(category.name, "Utilities")


class CategoryDetailSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_detail_data = {
            "category_id": self.category.id,
            "name": "Vegetables",
        }
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Vegetables"
        )

    def test_category_detail_serialization(self):
        serializer = CategoryDetailSerializer(self.category_detail)
        self.assertEqual(serializer.data["name"], "Vegetables")
        self.assertEqual(serializer.data["category"]["id"], self.category.id)
        self.assertEqual(serializer.data["category"]["name"], self.category.name)

    def test_category_detail_deserialization(self):
        serializer = CategoryDetailSerializer(data=self.category_detail_data)
        self.assertTrue(serializer.is_valid())
        category_detail = serializer.save()
        self.assertEqual(category_detail.name, "Vegetables")


class TransactionSerializerTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name="Test Account", balance=5000, type="Bank"
        )
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Vegetables"
        )
        self.transaction_data = {
            "account_id": self.account.id,
            "date": date(2024, 12, 23),
            "amount": 1000,
            "name": "Carrots",
            "category_detail_id": self.category_detail.id,
        }
        self.transaction = Transaction.objects.create(**self.transaction_data)

    def test_transaction_serialization(self):
        serializer = TransactionSerializer(self.transaction)
        self.assertEqual(serializer.data["name"], "Carrots")
        self.assertEqual(serializer.data["amount"], 1000)
        self.assertEqual(serializer.data["account"]["id"], self.account.id)
        self.assertEqual(serializer.data["account"]["name"], self.account.name)
        self.assertEqual(serializer.data["account"]["balance"], self.account.balance)
        self.assertEqual(serializer.data["account"]["type"], self.account.type)
        self.assertEqual(
            serializer.data["category_detail"]["id"], self.category_detail.id
        )
        self.assertEqual(
            serializer.data["category_detail"]["name"], self.category_detail.name
        )

    def test_transaction_deserialization(self):
        serializer = TransactionSerializer(data=self.transaction_data)
        self.assertTrue(serializer.is_valid())
        transaction = serializer.save()
        self.assertEqual(transaction.name, "Carrots")


class MonthlySerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Fruits"
        )
        self.monthly_data = {
            "category_detail_id": self.category_detail.id,
            "amount": 3000,
            "date": 202312,
        }
        self.monthly = Monthly.objects.create(**self.monthly_data)

    def test_monthly_serialization(self):
        serializer = MonthlySerializer(self.monthly)
        self.assertEqual(serializer.data["amount"], 3000)
        self.assertEqual(serializer.data["date"], 202312)
        self.assertEqual(
            serializer.data["category_detail"]["id"], self.category_detail.id
        )
        self.assertEqual(
            serializer.data["category_detail"]["name"], self.category_detail.name
        )

    def test_monthly_deserialization(self):
        serializer = MonthlySerializer(data=self.monthly_data)
        self.assertTrue(serializer.is_valid())
        monthly = serializer.save()
        self.assertEqual(monthly.amount, 3000)
        self.assertEqual(monthly.date, 202312)
