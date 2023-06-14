from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class MoreArtists(models.Model):
    difartistNames = models.CharField(_("All Artist Names"), max_length=50)
    difartistsThumbnail = models.ImageField(_("Artists Thumbnail"),upload_to='thumbnail/',help_text=".jpg,.png ,.jpeg, .gif, .svg supported")

    def __str__(self):
        return self.difartistNames 

class Artist(models.Model):
    artistName = models.CharField(_("Artist Name"), max_length=50)
    created = models.DateTimeField(_("Artist created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest artist update"), auto_now=True)

class Meta:
    verbose_name = _("Artist")
    verbose_name_plural = _("Artists")

    def __str__(self):
        return self.artistName    
    
class Song(models.Model):
    songThumbnail = models.ImageField(_("Song Thumbnail"),upload_to='thumbnail/',help_text=".jpg,.png ,.jpeg, .gif, .svg supported")
    song = models.FileField(_("Song"), upload_to='songs/', help_text=".mp3 spported only")
    songName = models.CharField(_("Song Name") , max_length=50)
    created = models.DateTimeField(_("Song created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest song update"), auto_now=True)

    class Meta:
     verbose_name = _("Song")
     verbose_name_plural = _("Songs")

    def __str__(self):
        return self.songName

class Songs(models.Model):
    songThumbnails = models.ImageField(_("Song Thumbnails"),upload_to='thumbnail/',help_text=".jpg,.png ,.jpeg, .gif, .svg supported")
    songs = models.FileField(_("Songs"), upload_to='songs/', help_text=".mp3 spported only")
    songNames = models.CharField(_("Song Names") , max_length=50)
    created = models.DateTimeField(_("Songs created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest songs update"), auto_now=True)

    def __str__(self):
        return self.songNames

class Video(models.Model):
    video = models.FileField(_("Video"), upload_to='videos/', help_text=".mp4 spported only")
    videoName = models.CharField(_("Video Name") , max_length=50)
  

    class Meta:
     verbose_name = _("Video")
     verbose_name_plural = _("Videos")

    def __str__(self):
        return self.videoName    