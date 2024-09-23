import os

from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from .managers import GameManager



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

# Global Variables
User = get_user_model()



class Publisher(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name
    
       
class DeveloperTeam(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name


    
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    cover = models.ImageField(upload_to=game_upload_path, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True, blank=True)
    developer = models.ForeignKey(DeveloperTeam, on_delete=models.PROTECT, null=True, blank=True)
    published_date = models.DateField(blank=True, null=True)
    
    # Custom Model Manager
    objects = GameManager()
    
    def __str__(self) -> str:
        return self.title
    
    # @property
    # def get_games_by_genre(self):
    #     return self.genres.filter(self.genre)
    
    


class UserGameStatus(models.Model):
    STATUS_CHOICES = [
        ('playing', 'Playing'),
        ('completed', 'Completed'),
        ('want_to_play', 'Want to Play'),
        ('paused', 'Paused'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'game')
        
        
    def __str__(self) -> str:
        return f"{self.user} - {self.game} ({self.status})"
    
    
    
