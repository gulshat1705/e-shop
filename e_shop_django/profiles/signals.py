from django.dispatch import receiver
from djoser.signals import user_registered

from profiles.models import Profile

@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):
    ''' create user profile during registration '''
    data = request.data

    Profile.objects.create(
        user=user,
        name=data.get("name", ""),
        address=data.get("address", "")
    )