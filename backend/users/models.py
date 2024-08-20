from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.conf import settings
# Create your models here.

class BaseUser(AbstractUser):
    pass


def profile_pic_path(filename):
    # Upload PATH => MEDIA_ROOT/ profile_picture
    return f'profile_picture/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='profile', unique=True)
    profile = models.ImageField(upload_to=profile_pic_path, null=True, blank=True)
    bio = models.TextField(max_length=255, blank=True, null=True, default='<blank>')
    
    def __str__(self) -> str:
        return f"{self.user.username}"
