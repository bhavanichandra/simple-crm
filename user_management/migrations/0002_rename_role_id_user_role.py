# Generated by Django 3.2.9 on 2021-11-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role_id',
            new_name='role',
        ),
    ]
