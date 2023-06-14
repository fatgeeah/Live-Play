# Generated by Django 4.2 on 2023-04-20 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50, verbose_name='Album Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Album created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest album update')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=50, verbose_name='Artist Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Artist created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest artist update')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songThumbnail', models.ImageField(help_text='.jpg,.png ,.jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Song Thumbnail')),
                ('song', models.FileField(help_text='.mp3 spported only', upload_to='songs/', verbose_name='Song')),
                ('songName', models.CharField(max_length=50, verbose_name='Song Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Song created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest song update')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicApp.album', verbose_name='Song Album')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicApp.artist', verbose_name='Artist Album'),
        ),
    ]
