# Generated by Django 3.2.7 on 2021-09-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=10)),
                ('choice', models.CharField(max_length=100)),
            ],
        ),
    ]
