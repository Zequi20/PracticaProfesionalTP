# Generated by Django 4.2 on 2023-05-26 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('ci', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('id_ciudad', models.ForeignKey(blank=True, db_column='id_ciudad', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
                ('id_ciudad', models.ForeignKey(blank=True, db_column='id_ciudad', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.SmallIntegerField(blank=True, null=True)),
                ('precio', models.PositiveBigIntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('capacidad', models.PositiveIntegerField()),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
                ('id_hotel', models.ForeignKey(blank=True, db_column='id_hotel', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('ci', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('id_ciudad', models.ForeignKey(blank=True, db_column='id_ciudad', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_departamento',
            field=models.ForeignKey(blank=True, db_column='id_departamento', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.departamento'),
        ),
    ]
