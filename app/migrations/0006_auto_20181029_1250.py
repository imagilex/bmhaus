# Generated by Django 2.0.7 on 2018-10-29 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181029_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usocfdi',
            field=models.ForeignKey(blank=True, limit_choices_to={'catalogo__idsat': 'UsoCFDi'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente_usocfdi', to='cfdi.OpcionCatalogoSAT'),
        ),
    ]