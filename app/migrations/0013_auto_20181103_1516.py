# Generated by Django 2.0.7 on 2018-11-03 21:16

import app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181103_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fecha_de_recepcion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='hora_de_recepcion',
            field=models.TimeField(default=app.models.getTime),
        ),
    ]
