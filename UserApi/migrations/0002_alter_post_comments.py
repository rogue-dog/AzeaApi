# Generated by Django 3.2.7 on 2021-09-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.JSONField(default='{  }'),
        ),
    ]
