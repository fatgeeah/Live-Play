from django.contrib import admin
from .models import Artist, Song ,  Video , Songs ,MoreArtists
# Register your models here.

@admin.register(MoreArtists)
class MoreArtistsAdmin(admin.ModelAdmin):
    list_display = ( "difartistNames" , "difartistsThumbnail" )

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ( "video" , "videoName" )
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id" , "artistName" , "created" , "last_updated")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id" ,"song","songName","songThumbnail", "created" , "last_updated")    

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("id" ,"songs","songNames","songThumbnails", "created" , "last_updated")    
 