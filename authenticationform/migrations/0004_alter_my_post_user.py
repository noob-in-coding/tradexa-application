# Generated by Django 3.2 on 2021-05-27 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationform', '0003_auto_20210527_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticationform.my_user'),
        ),
    ]