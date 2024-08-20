from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BaseUser as User, UserProfile as Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)