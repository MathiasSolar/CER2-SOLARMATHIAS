# Generated by Django 4.1.3 on 2022-11-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_alter_recepcion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='nombre',
            field=models.CharField(default='sin nombre', max_length=30),
            preserve_default=False,
        ),
    ]
