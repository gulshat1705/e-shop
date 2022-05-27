from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=150, blank=True, null=True)
    address = models.CharField('address', max_length=300, blank=True, null=True)


    def __str__(self):
        return f'{self.name} /{self.user.email}'
