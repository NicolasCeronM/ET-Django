# Generated by Django 4.2.1 on 2023-07-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appsuscripciones', '0005_alter_suscripcion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]