# Generated by Django 5.0.7 on 2024-07-28 19:55

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BizningMahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[410, 290], upload_to='media/')),
                ('nomi', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
