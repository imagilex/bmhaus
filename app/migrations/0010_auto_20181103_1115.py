# Generated by Django 2.0.7 on 2018-11-03 17:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('initsys', '0005_auto_20181024_1624'),
        ('app', '0009_auto_20181030_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvanceEnFlujo',
            fields=[
                ('idavanceenflujo', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.TextField()),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='avanceenflujo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.AlterModelOptions(
            name='doctoordenreparacion',
            options={'ordering': ['-fecha_de_recepcion', '-hora_de_recepcion']},
        ),
        migrations.RemoveField(
            model_name='doctoordenreparacion',
            name='fecha_y_hora_de_recepcion',
        ),
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='fecha_de_recepcion',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='hora_de_recepcion',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
