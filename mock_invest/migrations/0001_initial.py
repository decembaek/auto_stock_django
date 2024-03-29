# Generated by Django 5.0.2 on 2024-02-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MockInvestAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("account_name", models.CharField(max_length=100)),
                (
                    "initial_balance",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=20
                    ),
                ),
                (
                    "current_balance",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="StockPostion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("stock_counts", models.PositiveIntegerField()),
                (
                    "average_buy_price",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("BUY", "BUY"), ("SELL", "SELL")], max_length=4
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "price_per_share",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
