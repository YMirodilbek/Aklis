# Generated by Django 5.0.7 on 2024-08-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_mahsulotlar_sarlavha_en_mahsulotlar_sarlavha_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulotlar',
            name='sarlavha',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mahsulotlar',
            name='sarlavha_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='mahsulotlar',
            name='sarlavha_ru',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='mahsulotlar',
            name='sarlavha_uz',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
