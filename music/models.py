from django.db import models

# Create your models here.
class Album(models.Model):
    srtist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genere = models.CharField(max_length=100)
    albun_logo = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.foreignkey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)