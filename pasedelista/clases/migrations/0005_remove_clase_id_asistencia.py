# Generated by Django 3.1.4 on 2020-12-07 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0004_auto_20201206_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='id_asistencia',
        ),
    ]
