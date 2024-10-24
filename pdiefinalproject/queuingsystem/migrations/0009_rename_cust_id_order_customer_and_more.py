# Generated by Django 5.0 on 2024-10-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queuingsystem", "0008_order_orderitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="cust_id",
            new_name="customer",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_time",
            new_name="date_ordered",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="staff_id",
            new_name="staff",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="total_cost",
            new_name="total_price",
        ),
        migrations.RenameField(
            model_name="orderitem",
            old_name="item_price",
            new_name="price",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_status",
        ),
        migrations.RemoveField(
            model_name="order",
            name="queue_number",
        ),
        migrations.RemoveField(
            model_name="order",
            name="table_number",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="customer",
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]