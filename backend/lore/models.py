from django.db import models
from games.models import Game


class Lore(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='lore')
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    
    
    def __str__(self):
        return f"{self.game} - {self.title[:10]}"



class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    role = models.CharField()