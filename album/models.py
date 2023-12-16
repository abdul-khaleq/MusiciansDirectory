from django.db import models
from musician.models import MusicianModel

# Create your models here.
class AlbumModel(models.Model):
    albumName = models.CharField(max_length=55)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    albumReleaseDate = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=((i,i) for i in range(1, 6)))

    def __str__(self):
        return f"Album name: {self.albumName}"