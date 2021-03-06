# Generated by Django 2.0.7 on 2018-10-15 00:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.Permission')),
                ('idpermiso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('mostrar_como', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('vista', models.CharField(blank=True, max_length=100, null=True)),
                ('es_operacion', models.BooleanField(default=False)),
                ('posicion', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Permiso')),
                ('permiso_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Permiso')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Permiso')),
            ],
            options={
                'ordering': ['posicion', 'nombre'],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('contraseña', models.CharField(max_length=250)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='usuarios')),
                ('depende_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
