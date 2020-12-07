# Generated by Django 3.1.4 on 2020-12-07 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0005_remove_clase_id_asistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('periodo', models.CharField(max_length=10)),
                ('año', models.IntegerField(default=2020)),
                ('id_clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clases.clase')),
            ],
        ),
    ]
