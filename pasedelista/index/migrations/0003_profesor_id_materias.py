# Generated by Django 3.1.4 on 2020-12-07 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_profesor'),
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='id_materias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.materia'),
        ),
    ]
