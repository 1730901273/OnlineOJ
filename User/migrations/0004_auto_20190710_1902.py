# Generated by Django 2.2.3 on 2019-07-10 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_users_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='icon',
            new_name='avatar',
        ),
    ]
