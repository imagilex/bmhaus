# Generated by Django 2.0.7 on 2018-12-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20181119_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='identificador',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
