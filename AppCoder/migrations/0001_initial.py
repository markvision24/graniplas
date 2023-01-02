# Generated by Django 4.1.4 on 2022-12-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('Nombre_Titanio', models.CharField(max_length=40)),
                ('Titanio', models.IntegerField()),
                ('Nombre_Amarillo_Bayer', models.CharField(max_length=40)),
                ('Amarillo_Bayer', models.IntegerField()),
                ('Nombre_Amarillo_Vivo', models.CharField(max_length=40)),
                ('Amarillo_Vivo', models.IntegerField()),
                ('Nombre_Amarillo_AL90', models.CharField(max_length=40)),
                ('Amarillo_AL90', models.IntegerField()),
                ('Nombre_Azul', models.CharField(max_length=40)),
                ('Azul', models.IntegerField()),
                ('Nombre_Rojo_Bayer', models.CharField(max_length=40)),
                ('Rojo_Bayer', models.IntegerField()),
                ('Nombre_Rojo_Vivo', models.CharField(max_length=40)),
                ('Rojo_Vivo', models.IntegerField()),
                ('Nombre_Negro', models.CharField(max_length=40)),
                ('Negro', models.IntegerField()),
                ('Nombre_Tinta_Azul', models.CharField(max_length=40)),
                ('Tinta_Azul', models.IntegerField()),
                ('Nombre_Tinta_Verde', models.CharField(max_length=40)),
                ('Tinta_Verde', models.IntegerField()),
                ('Nombre_Tinta_Roja', models.CharField(max_length=40)),
                ('Tinta_Roja', models.IntegerField()),
                ('Nombre_Tinta_Violeta', models.CharField(max_length=40)),
                ('Tinta_Violeta', models.IntegerField()),
                ('Nombre_Tinta_Fucsia', models.CharField(max_length=40)),
                ('Tinta_Fucsia', models.IntegerField()),
                ('Agua', models.IntegerField()),
                ('Resina', models.IntegerField()),
                ('Talco', models.IntegerField()),
                ('Arena', models.IntegerField()),
                ('Celulosa', models.IntegerField()),
                ('Cuarzo', models.IntegerField()),
                ('AntiBacterial', models.IntegerField()),
                ('AntiEspumante', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.IntegerField()),
                ('Nombres', models.CharField(max_length=40)),
                ('Apellidos', models.CharField(max_length=40)),
                ('Cargo', models.CharField(max_length=40)),
                ('Año_Nacimiento', models.IntegerField()),
                ('RH', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_2', models.IntegerField()),
                ('Nombre_Titanio_2', models.CharField(max_length=40)),
                ('Titanio_2', models.IntegerField()),
                ('Nombre_Amarillo_Bayer_2', models.CharField(max_length=40)),
                ('Amarillo_Bayer_2', models.IntegerField()),
                ('Nombre_Amarillo_Vivo_2', models.CharField(max_length=40)),
                ('Amarillo_Vivo_2', models.IntegerField()),
                ('Nombre_Amarillo_AL90_2', models.CharField(max_length=40)),
                ('Amarillo_AL90_2', models.IntegerField()),
                ('Nombre_Azul_2', models.CharField(max_length=40)),
                ('Azul_2', models.IntegerField()),
                ('Nombre_Rojo_Bayer_2', models.CharField(max_length=40)),
                ('Rojo_Bayer_2', models.IntegerField()),
                ('Nombre_Rojo_Vivo_2', models.CharField(max_length=40)),
                ('Rojo_Vivo_2', models.IntegerField()),
                ('Nombre_Negro_2', models.CharField(max_length=40)),
                ('Negro_2', models.IntegerField()),
                ('Nombre_Tinta_Azul_2', models.CharField(max_length=40)),
                ('Tinta_Azul_2', models.IntegerField()),
                ('Nombre_Tinta_Verde_2', models.CharField(max_length=40)),
                ('Tinta_Verde_2', models.IntegerField()),
                ('Nombre_Tinta_Roja_2', models.CharField(max_length=40)),
                ('Tinta_Roja_2', models.IntegerField()),
                ('Nombre_Tinta_Violeta_2', models.CharField(max_length=40)),
                ('Tinta_Violeta_2', models.IntegerField()),
                ('Nombre_Tinta_Fucsia_2', models.CharField(max_length=40)),
                ('Tinta_Fucsia_2', models.IntegerField()),
                ('Agua_2', models.IntegerField()),
                ('Resina_2', models.IntegerField()),
                ('Talco_2', models.IntegerField()),
                ('Celulosa_2', models.IntegerField()),
                ('AntiBacterial_2', models.IntegerField()),
                ('AntiEspumante_2', models.IntegerField()),
            ],
        ),
    ]
