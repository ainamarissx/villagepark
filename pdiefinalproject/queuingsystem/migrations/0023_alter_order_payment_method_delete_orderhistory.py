# Generated by Django 5.0 on 2024-10-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0022_order_queue_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                blank=True, default="Unpaid", max_length=50, null=True
            ),
        ),
        migrations.DeleteModel(
            name="OrderHistory",
        ),
    ]
