# Generated by Django 5.0.1 on 2024-01-20 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
