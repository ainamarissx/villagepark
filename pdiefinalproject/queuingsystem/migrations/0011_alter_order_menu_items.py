# Generated by Django 5.0 on 2024-10-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0010_order_menu_items_delete_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="menu_items",
            field=models.TextField(),
        ),
    ]
