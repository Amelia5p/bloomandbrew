# Generated by Django 5.2 on 2025-05-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bundle_of_the_week',
            field=models.BooleanField(default=False),
        ),
    ]
