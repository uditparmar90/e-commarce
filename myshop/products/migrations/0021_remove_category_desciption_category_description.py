# Generated by Django 5.0.1 on 2024-01-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='desciption',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=50, null=True),
        ),
    ]