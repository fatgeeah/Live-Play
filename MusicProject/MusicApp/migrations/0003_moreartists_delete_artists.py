# Generated by Django 4.1.7 on 2023-04-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApp', '0002_artists'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreArtists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difartistNames', models.CharField(max_length=50, verbose_name='All Artist Names')),
                ('difartistsThumbnail', models.ImageField(help_text='.jpg,.png ,.jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Artists Thumbnail')),
            ],
        ),
        migrations.DeleteModel(
            name='Artists',
        ),
    ]