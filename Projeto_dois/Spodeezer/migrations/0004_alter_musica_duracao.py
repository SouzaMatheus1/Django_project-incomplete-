# Generated by Django 4.0.5 on 2022-06-02 19:21

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Spodeezer', '0003_musica_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.TimeField(verbose_name=django.forms.fields.NullBooleanField),
        ),
    ]
