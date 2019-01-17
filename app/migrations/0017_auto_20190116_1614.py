# Generated by Django 2.0.7 on 2019-01-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_doctoordenreparacion_identificador'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='kilometros',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='observaciones',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doctoordenreparacion',
            name='tanque_de_gasolina',
            field=models.CharField(choices=[('0', '0'), ('1_4', '1/4'), ('1_2', '1/2'), ('3_4', '3/4'), ('4_4', '4/4')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='firma_del_consumidor',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='firma_del_prestador_del_servicio',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_frente',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_kilometros',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_lateral_derecho',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_lateral_izquierdo',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_superior',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_tanque_de_gasolina',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fotografia_trasera',
            field=models.ImageField(blank=True, default='', upload_to='doctoordenreparacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='servicio_solicitado',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
