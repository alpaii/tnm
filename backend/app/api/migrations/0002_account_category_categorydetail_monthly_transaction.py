# Generated by Django 5.1.4 on 2024-12-29 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("balance", models.BigIntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Bank", "Bank"),
                            ("Card", "Card"),
                            ("Deposit", "Deposit"),
                            ("Cash", "Cash"),
                            ("Person", "Person"),
                            ("Asset", "Asset"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CategoryDetail",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details",
                        to="api.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Monthly",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("amount", models.BigIntegerField()),
                ("date", models.PositiveIntegerField()),
                (
                    "category_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="monthly_expenses",
                        to="api.categorydetail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField()),
                ("amount", models.BigIntegerField()),
                ("name", models.CharField(max_length=255)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="api.account",
                    ),
                ),
                (
                    "category_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="api.categorydetail",
                    ),
                ),
            ],
        ),
    ]
