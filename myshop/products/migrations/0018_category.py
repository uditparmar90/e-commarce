# Generated by Django 5.0.1 on 2024-01-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_address_brand_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desciption', models.CharField(max_length=50)),
            ],
        ),
    ]
