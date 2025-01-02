from django.db import models


# 테스트 테이블
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    TYPE_CHOICES = [
        ("Bank", "Bank"),
        ("Card", "Card"),
        ("Deposit", "Deposit"),
        ("Cash", "Cash"),
        ("Person", "Person"),
        ("Asset", "Asset"),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    balance = models.BigIntegerField()
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="details"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    date = models.DateField()  # DateTimeField -> DateField
    amount = models.BigIntegerField()
    name = models.CharField(max_length=255)
    category_detail = models.ForeignKey(
        CategoryDetail, on_delete=models.CASCADE, related_name="transactions"
    )

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Monthly(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_detail = models.ForeignKey(
        CategoryDetail, on_delete=models.CASCADE, related_name="monthly_expenses"
    )
    amount = models.BigIntegerField()
    date = (
        models.PositiveIntegerField()
    )  # Storing year-month as an integer, e.g., 202312 for December 2023

    def __str__(self):
        return f"{self.category_detail.name} - {self.amount} ({self.date})"
