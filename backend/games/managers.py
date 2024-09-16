from django.db import models


class GameManager(models.Manager):
    def get_by_genre(self, genre_name):
        return self.filter(genres__name=genre_name)