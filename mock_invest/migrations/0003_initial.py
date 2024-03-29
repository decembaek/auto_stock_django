# Generated by Django 5.0.2 on 2024-02-23 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("korea_stock", "0002_alter_ksiccodemodel_id"),
        ("mock_invest", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="mockinvestaccount",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="stockpostion",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mock_invest.mockinvestaccount",
            ),
        ),
        migrations.AddField(
            model_name="stockpostion",
            name="stock",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="korea_stock.stockcodemodel",
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mock_invest.mockinvestaccount",
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="stock",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="korea_stock.stockcodemodel",
            ),
        ),
    ]
