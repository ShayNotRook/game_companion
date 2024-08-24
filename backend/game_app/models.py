from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self) -> str:
        return self.title