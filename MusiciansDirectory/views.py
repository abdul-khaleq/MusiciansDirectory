from django.shortcuts import render
from album.models import AlbumModel

def home(request):
    albums = AlbumModel.objects.all()
    return render(request, 'home.html', {'albums':albums})