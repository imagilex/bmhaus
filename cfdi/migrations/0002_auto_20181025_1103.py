# Generated by Django 2.0.7 on 2018-10-25 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfdi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 25, 11, 3, 6, 688609)),
        ),
    ]