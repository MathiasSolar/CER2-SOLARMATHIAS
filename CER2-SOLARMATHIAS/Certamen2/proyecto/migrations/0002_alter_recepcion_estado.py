# Generated by Django 4.1.3 on 2022-11-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepcion',
            name='estado',
            field=models.CharField(choices=[('entregado', 'entregado'), ('no entregado', 'no entregado')], max_length=30),
        ),
    ]
