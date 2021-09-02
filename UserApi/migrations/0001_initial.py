# Generated by Django 3.2.7 on 2021-09-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
# Asshole
    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('email', models.CharField(max_length=250,
                 primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=250)),
            ],
        ),
    ]
