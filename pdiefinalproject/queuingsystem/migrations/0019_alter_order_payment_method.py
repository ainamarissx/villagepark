# Generated by Django 5.0 on 2024-10-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0018_alter_order_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                blank=True, default="QR Code", max_length=50, null=True
            ),
        ),
    ]
