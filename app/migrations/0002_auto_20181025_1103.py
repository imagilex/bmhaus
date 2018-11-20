# Generated by Django 2.0.7 on 2018-10-25 16:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='residenciafiscal',
            field=models.ForeignKey(blank=True, limit_choices_to={'catalogo__idsat': 'Pais'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente_residenciafiscal', to='cfdi.OpcionCatalogoSAT'),
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fecha_y_hora_de_recepcion',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 25, 11, 3, 6, 797977)),
        ),
    ]
