# Generated by Django 5.1.1 on 2024-09-25 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_alter_device_date_verification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Device',
        ),
    ]
