# Generated by Django 4.2.9 on 2024-06-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Наименование')),
                ('subdivision', models.CharField(blank=True, max_length=400, null=True, verbose_name='Подразделение')),
                ('factory_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заводской Номер')),
                ('sensor', models.CharField(blank=True, max_length=200, null=True, verbose_name='Датчик')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='количество')),
                ('date_issued', models.DateField(verbose_name='Дата Выпуска')),
                ('date_entry', models.DateField(verbose_name='Дата Ввода')),
                ('date_verification', models.DateField(verbose_name='Дата Поверки')),
                ('repair_result', models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат Ремонта')),
                ('date_next_verification', models.DateField(verbose_name='Дата Следующей Поверки')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='Состояние')),
            ],
        ),
    ]
