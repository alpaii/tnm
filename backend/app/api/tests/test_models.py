from django.test import TestCase
from api.models import Account, Category, CategoryDetail, Account, Transaction, Monthly
from datetime import datetime


class AccountModelTest(TestCase):
    def setUp(self):
        # 테스트 데이터 생성
        self.account = Account.objects.create(
            name="Test Account", balance=1000, type="Checking"
        )

    def test_account_creation(self):
        # 계좌가 올바르게 생성되었는지 확인
        self.assertEqual(self.account.name, "Test Account")
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(self.account.type, "Checking")


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Groceries")


class CategoryDetailModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Vegetables"
        )

    def test_category_detail_creation(self):
        self.assertEqual(self.category_detail.name, "Vegetables")
        self.assertEqual(self.category_detail.category.name, "Groceries")

    def test_category_detail_string_representation(self):
        self.assertEqual(str(self.category_detail), "Vegetables")


class TransactionModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name="Checking Account", balance=5000, type="Checking"
        )
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Vegetables"
        )
        self.transaction = Transaction.objects.create(
            account=self.account,
            date=datetime(2023, 12, 23, 10, 0),
            amount=1000,
            name="Carrots",
            category_detail=self.category_detail,
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.name, "Carrots")
        self.assertEqual(self.transaction.amount, 1000)
        self.assertEqual(self.transaction.account.name, "Checking Account")
        self.assertEqual(self.transaction.category_detail.name, "Vegetables")

    def test_transaction_string_representation(self):
        self.assertEqual(str(self.transaction), "Carrots - 1000")


class MonthlyModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Fruits"
        )
        self.monthly = Monthly.objects.create(
            category_detail=self.category_detail, amount=3000, date=202312
        )

    def test_monthly_creation(self):
        self.assertEqual(self.monthly.amount, 3000)
        self.assertEqual(self.monthly.date, 202312)
        self.assertEqual(self.monthly.category_detail.name, "Fruits")

    def test_monthly_string_representation(self):
        self.assertEqual(str(self.monthly), "Fruits - 3000 (202312)")
