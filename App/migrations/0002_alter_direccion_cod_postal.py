# Generated by Django 4.2.1 on 2023-06-26 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='cod_postal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
