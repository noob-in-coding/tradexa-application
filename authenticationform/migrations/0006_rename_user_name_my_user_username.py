# Generated by Django 3.2 on 2021-05-28 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationform', '0005_alter_my_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_user',
            old_name='user_name',
            new_name='username',
        ),
    ]
