# Generated by Django 3.2.9 on 2021-11-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211124_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
