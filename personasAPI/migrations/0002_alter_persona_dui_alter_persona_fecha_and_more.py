# Generated by Django 4.0.3 on 2022-03-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personasAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dui',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
    ]