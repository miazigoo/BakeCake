# Generated by Django 4.2.3 on 2023-07-19 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cake",
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
                ("price", models.IntegerField(verbose_name="Стоимость торта")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cakes",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Торт",
                "verbose_name_plural": "Торты",
            },
        ),
        migrations.DeleteModel(
            name="CustomCake",
        ),
    ]
