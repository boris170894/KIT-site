# Generated by Django 4.2.2 on 2023-09-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_statesymbolsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statesymbolsmodel',
            name='desc',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='statesymbolsmodel',
            name='desc_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='statesymbolsmodel',
            name='desc_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
