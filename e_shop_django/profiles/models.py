from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings

from users_app.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=150, blank=True, null=True)
    address = models.CharField('address', max_length=300, blank=True, null=True)


    def __str__(self):
        return f'{self.name} /{self.user.email}'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()        



        
