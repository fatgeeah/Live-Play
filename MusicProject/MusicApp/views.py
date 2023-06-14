from django.shortcuts import render
from .models import Song , Video , Songs ,MoreArtists


def Search_Video(request):
      if request.method == "POST":
        searched =  request.POST['searched']
        allVideos = Video.objects.filter(videoName__contains=searched)
      return render(request,  "Search_Video.html" , {'searched':searched ,
                                                     'allVideos':allVideos}) 

def Search_Artist(request):
    if request.method == "POST":
        searched =  request.POST['searched']
        allArtists = MoreArtists.objects.filter(difartistNames__contains=searched)
        return render(request,  "Search_Artists.html" , {'searched':searched ,
                                                       'allArtists':allArtists})
    else:
        return render(request,  "Search_Artists.html" , {}) 

def Search_Music(request):
    if request.method == "POST":
        searched =  request.POST['searched']
        allSongs = Songs.objects.filter(songNames__contains=searched)
        return render(request,  "Search_Music.html" , {'searched':searched ,
                                                       'allSongs':allSongs})
    else:
        return render(request,  "Search_Music.html" , {}) 


def Artists_list(request):
    allArtists = MoreArtists.objects.all()
    return render(request, template_name="Artists_list.html", context={"allArtists":allArtists})


def videos(request):
        allVideos= Video.objects.all()
        return render(request, template_name="videos.html", context={"allVideos":allVideos})

def Music_list(request):
      allSongs = Songs.objects.all()
      return render(request, template_name="Music_list.html", context={"allSongs":allSongs})

def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "login.html")
