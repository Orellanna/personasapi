# Generated by Django 4.0.3 on 2022-03-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('dui', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
