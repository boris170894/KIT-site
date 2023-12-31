# Generated by Django 4.2.2 on 2023-06-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_name', models.CharField(max_length=200, verbose_name='Специальность')),
                ('spec_info', models.TextField(verbose_name='Описание')),
                ('spec_img', models.ImageField(blank=True, upload_to='upload/specs', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Специальности',
                'verbose_name_plural': 'Специальности',
            },
        ),
    ]
