# Generated by Django 2.0.7 on 2018-11-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initsys', '0006_alerta_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='fecha_alertado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alerta',
            name='fecha_no_mostrar',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alerta',
            name='fecha_alerta',
            field=models.DateField(),
        ),
    ]
