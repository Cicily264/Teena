# Generated by Django 4.2.4 on 2023-10-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
