# Generated by Django 4.0.5 on 2022-06-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_album', models.CharField(max_length=200)),
                ('ano', models.CharField(max_length=4)),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_musica', models.CharField(max_length=200)),
                ('duracao', models.FloatField(max_length=10.0)),
                ('compositor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_artista', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('ano', models.CharField(max_length=4)),
                ('album', models.ManyToManyField(to='Spodeezer.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(to='Spodeezer.musica'),
        ),
    ]
