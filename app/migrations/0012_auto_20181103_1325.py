# Generated by Django 2.0.7 on 2018-11-03 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20181103_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctoordenreparacion',
            old_name='fotografia_tracera',
            new_name='fotografia_trasera',
        ),
    ]
