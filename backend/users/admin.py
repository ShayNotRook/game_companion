from django.contrib import admin

from .models import UserProfile, BaseUser


class ProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'bio')
    fields = ('user', 'profile', 'bio')

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(BaseUser)
