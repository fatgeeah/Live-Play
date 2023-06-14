from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('Artists_list',views.Artists_list,name="Artists_list"),
    # path('music',views.music,name="music"),
    path('videos',views.videos,name="videos"),
    path('Music_list', views.Music_list, name='Music_list'),
    path('Search_Music',views.Search_Music,name="Search_Music"),
    path('Search_Artist',views.Search_Artist,name="Search_Artist"),
    path('Search_Video',views.Search_Video,name="Search_Video"),
]
