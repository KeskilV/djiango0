# Generated by Django 4.0.4 on 2022-05-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
        ),
        migrations.CreateModel(
            name='Diamonds4c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogr', models.CharField(max_length=20, verbose_name='Огранка')),
                ('col', models.CharField(max_length=3, verbose_name='Цвет')),
                ('cla', models.CharField(max_length=3, verbose_name='Чистота')),
                ('cut', models.CharField(max_length=1, verbose_name='Параметр огранки')),
                ('carat', models.FloatField(verbose_name='Карат')),
                ('pcs', models.IntegerField(verbose_name='Штук')),
            ],
            options={
                'verbose_name': 'Сертифицированный бриллиант',
                'verbose_name_plural': 'Сертифицированные бриллианты',
            },
        ),
    ]
