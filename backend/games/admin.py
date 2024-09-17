from django.contrib import admin
from .models import Game, Genre, Publisher, DeveloperTeam
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genres', 'developer', 'publisher')
    filter_horizontal = ('genres',)
    
    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    
    display_genres.short_description = 'Genres'


admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(DeveloperTeam)