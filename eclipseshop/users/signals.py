from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def profile_update(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            user_name = user.username,
        )

@receiver(post_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()
