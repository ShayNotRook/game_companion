import os

from django.db import models
from django.utils.text import slugify

# Util function
def game_upload_path(instance, filename):
    # Debugging statements to check values
    print(f"Title: {instance.title}, Filename: {filename}")
    
    if not instance.title:
        raise ValueError("The game must have a title before uploading an image.")
    
    sanitized_title = slugify(instance.title) if instance.title else 'untitle-game'
    
    if not filename:
        raise ValueError("The file must have a valid name.")
    
    return os.path.join('games', sanitized_title, filename)
    
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    cover = models.ImageField(upload_to=game_upload_path, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title