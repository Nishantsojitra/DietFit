# Generated by Django 4.1.13 on 2024-09-24 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_buy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
