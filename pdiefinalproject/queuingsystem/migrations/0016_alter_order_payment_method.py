# Generated by Django 5.0 on 2024-10-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0015_alter_order_menu_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(max_length=50),
        ),
    ]