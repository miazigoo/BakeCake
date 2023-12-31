# Generated by Django 4.2.3 on 2023-07-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cake_delete_customcake'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='cake',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='картинка'),
            preserve_default=False,
        ),
    ]
