# Generated by Django 3.0.7 on 2020-09-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200913_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', null=True, upload_to='media/Blog', verbose_name='Изображение'),
        ),
    ]