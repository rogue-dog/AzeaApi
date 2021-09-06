# Generated by Django 3.2.7 on 2021-09-06 17:05

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('uploader_id', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=10)),
                ('likes', models.CharField(default='', max_length=10000, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('comments', models.JSONField(default='{  }')),
                ('timestamp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('email', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=250)),
            ],
        ),
    ]
