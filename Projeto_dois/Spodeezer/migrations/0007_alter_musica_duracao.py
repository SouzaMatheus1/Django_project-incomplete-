# Generated by Django 4.0.5 on 2022-06-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spodeezer', '0006_alter_musica_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.FloatField(max_length=10.0),
        ),
    ]
