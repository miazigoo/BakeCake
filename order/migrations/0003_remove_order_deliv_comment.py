# Generated by Django 4.2.3 on 2023-07-19 00:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_order_deliv_comment_order_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="deliv_comment",
        ),
    ]
