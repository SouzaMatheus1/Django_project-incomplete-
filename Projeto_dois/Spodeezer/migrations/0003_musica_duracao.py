# Generated by Django 4.0.5 on 2022-06-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spodeezer', '0002_remove_musica_duracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='duracao',
            field=models.TimeField(default="00:00"),
        ),
    ]
