# Generated by Django 5.0.7 on 2024-07-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bizningmahsulot_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bizningmahsulot',
            name='rasm',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
