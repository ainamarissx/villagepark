# Generated by Django 5.0 on 2024-10-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0025_alter_order_receipt"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]
