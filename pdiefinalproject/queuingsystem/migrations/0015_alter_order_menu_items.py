# Generated by Django 5.0 on 2024-10-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0014_alter_order_receipt_orderhistory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="menu_items",
            field=models.JSONField(default=dict),
        ),
    ]
