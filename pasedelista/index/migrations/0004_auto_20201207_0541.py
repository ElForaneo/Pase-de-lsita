# Generated by Django 3.1.4 on 2020-12-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
        ('index', '0003_profesor_id_materias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Profesore',
        ),
    ]
