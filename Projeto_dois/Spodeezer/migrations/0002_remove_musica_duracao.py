# Generated by Django 4.0.5 on 2022-06-02 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spodeezer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='duracao',
        ),
    ]
