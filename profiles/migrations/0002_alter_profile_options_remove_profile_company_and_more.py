# Generated by Django 5.1.1 on 2024-09-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_worker',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='timesheet_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='update_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
