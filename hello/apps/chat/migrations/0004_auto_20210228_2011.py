# Generated by Django 3.0.7 on 2021-02-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210228_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='category',
            field=models.IntegerField(blank=True, choices=[('0', 'Нужна помощь в финансовой грамотносте'), ('3', 'Есть ошибка на сайте'), ('2', 'У меня есть личный вопрос'), ('1', 'Давай выпьем кофе')], default='0', null=True),
        ),
    ]
