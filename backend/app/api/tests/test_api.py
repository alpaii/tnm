from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date
from api.models import Account, Category, CategoryDetail, Transaction, Monthly


class AccountAPITestCase(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name="Checking Account", balance=5000, type="Bank"
        )
        self.account_list_url = reverse("account-list")
        self.account_detail_url = reverse("account-detail", args=[self.account.id])

    def test_get_account_list(self):
        response = self.client.get(self.account_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Checking Account")

    def test_create_account(self):
        new_account_data = {
            "name": "Savings Account",
            "balance": 2000,
            "type": "Bank",
        }
        response = self.client.post(self.account_list_url, new_account_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 2)

    def test_update_account(self):
        updated_account_data = {
            "name": "Updated Account",
            "balance": 3000,
            "type": "Card",
        }
        response = self.client.put(self.account_detail_url, updated_account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.name, "Updated Account")
        self.assertEqual(self.account.balance, 3000)

    def test_delete_account(self):
        response = self.client.delete(self.account_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Account.objects.count(), 0)


class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_list_url = reverse("category-list")
        self.category_detail_url = reverse("category-detail", args=[self.category.id])

    def test_get_category_list(self):
        response = self.client.get(self.category_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Groceries")

    def test_create_category(self):
        new_category_data = {"name": "Utilities"}
        response = self.client.post(self.category_list_url, new_category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_update_category(self):
        updated_category_data = {"name": "Updated Category"}
        response = self.client.put(self.category_detail_url, updated_category_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Updated Category")

    def test_delete_category(self):
        response = self.client.delete(self.category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


class CategoryDetailAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Groceries")
        self.category_detail = CategoryDetail.objects.create(
            category=self.category, name="Vegetables"
        )
        self.category_detail_list_url = reverse("categorydetail-list")
        self.category_detail_url = reverse(
            "categorydetail-detail", args=[self.category_detail.id]
        )

    def test_get_category_detail_list(self):
        response = self.client.get(self.category_detail_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Vegetables")

    def test_create_category_detail(self):
        new_category_detail_data = {"category_id": self.category.id, "name": "Fruits"}
        response = self.client.post(
            self.category_detail_list_url, new_category_detail_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CategoryDetail.objects.count(), 2)

    def test_update_category_detail(self):
        updated_category_detail_data = {
            "category_id": self.category.id,
            "name": "Updated Vegetables",
        }
        response = self.client.put(
            self.category_detail_url, updated_category_detail_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category_detail.refresh_from_db()
        self.assertEqual(self.category_detail.name, "Updated Vegetables")

    def test_delete_category_detail(self):
        response = self.client.delete(self.category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CategoryDetail.objects.count(), 0)


# class MonthlyAPITestCase(APITestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name="Groceries")
#         self.category_detail = CategoryDetail.objects.create(
#             category=self.category, name="Vegetables"
#         )
#         self.monthly = Monthly.objects.create(
#             category_detail=self.category_detail, amount=3000, date=202312
#         )
#         self.monthly_list_url = reverse("monthly-list")
#         self.monthly_detail_url = reverse("monthly-detail", args=[self.monthly.id])

#     def test_get_monthly_list(self):
#         response = self.client.get(self.monthly_list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["amount"], 3000)

#     def test_create_monthly(self):
#         new_monthly_data = {
#             "category_detail_id": self.category_detail.id,
#             "amount": 5000,
#             "date": 202401,
#         }
#         response = self.client.post(self.monthly_list_url, new_monthly_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Monthly.objects.count(), 2)

#     def test_update_monthly(self):
#         updated_monthly_data = {
#             "category_detail_id": self.category_detail.id,
#             "amount": 4000,
#             "date": 202402,
#         }
#         response = self.client.put(self.monthly_detail_url, updated_monthly_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.monthly.refresh_from_db()
#         self.assertEqual(self.monthly.amount, 4000)
#         self.assertEqual(self.monthly.date, 202402)

#     def test_delete_monthly(self):
#         response = self.client.delete(self.monthly_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Monthly.objects.count(), 0)


# class TransactionAPITestCase(APITestCase):
#     def setUp(self):
#         # 테스트 데이터 생성
#         self.account = Account.objects.create(
#             name="Test Account", balance=5000, type="Bank"
#         )
#         self.category = Category.objects.create(name="Groceries")
#         self.category_detail = CategoryDetail.objects.create(
#             category=self.category, name="Vegetables"
#         )
#         self.transaction = Transaction.objects.create(
#             account=self.account,
#             date=date(2023, 12, 23),
#             amount=1000,
#             name="Carrots",
#             category_detail=self.category_detail,
#         )
#         self.transaction_list_url = reverse("transaction-list")  # /api/transactions/
#         self.transaction_detail_url = reverse(
#             "transaction-detail", args=[self.transaction.id]
#         )  # /api/transactions/<id>/

#     def test_get_transaction_list(self):
#         # GET 요청: 전체 Transaction 조회
#         response = self.client.get(self.transaction_list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)  # 데이터 개수 확인
#         self.assertEqual(response.data[0]["name"], "Carrots")

#     def test_get_transaction_detail(self):
#         # GET 요청: 특정 Transaction 조회
#         response = self.client.get(self.transaction_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["name"], "Carrots")
#         self.assertEqual(response.data["amount"], 1000)

#     def test_create_transaction(self):
#         # POST 요청: 새로운 Transaction 생성
#         new_transaction_data = {
#             "account_id": self.account.id,
#             "date": "2023-12-24",  # 날짜는 ISO 8601 형식
#             "amount": 1500,
#             "name": "Potatoes",
#             "category_detail_id": self.category_detail.id,
#         }
#         response = self.client.post(self.transaction_list_url, new_transaction_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Transaction.objects.count(), 2)  # 데이터 개수 증가 확인
#         self.assertEqual(Transaction.objects.last().name, "Potatoes")

#     def test_update_transaction(self):
#         # PUT 요청: 기존 Transaction 수정
#         updated_transaction_data = {
#             "account_id": self.account.id,
#             "date": "2023-12-25",
#             "amount": 2000,
#             "name": "Updated Carrots",
#             "category_detail_id": self.category_detail.id,
#         }
#         response = self.client.put(
#             self.transaction_detail_url, updated_transaction_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.transaction.refresh_from_db()  # 데이터베이스에서 최신 데이터 가져오기
#         self.assertEqual(self.transaction.name, "Updated Carrots")
#         self.assertEqual(self.transaction.amount, 2000)

#     def test_delete_transaction(self):
#         # DELETE 요청: Transaction 삭제
#         response = self.client.delete(self.transaction_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Transaction.objects.count(), 0)  # 데이터 개수 확인
