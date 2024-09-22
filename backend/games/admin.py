from django.contrib import admin
from .models import Game, Genre, Publisher, DeveloperTeam, UserGameStatus
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genres', 'developer', 'publisher', 'published_date')
    filter_horizontal = ('genres',)
    
    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    
    display_genres.short_description = 'Genres'


class UserGameStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'status', 'added_at')

admin.site.register(Game, GameAdmin)
admin.site.register(UserGameStatus, UserGameStatusAdmin)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(DeveloperTeam)