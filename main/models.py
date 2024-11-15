from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define the Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='profile/default_profile.jpg', 
        upload_to='profile'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal to automatically create/update a profile when a user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        instance.get_profile()

# Define the safe profile accessor function
def get_profile(self):
    # Ensure profile creation only for non-superuser accounts or when necessary
    if hasattr(self, '_profile_cache'):
        return self._profile_cache

    if self.is_active and not self.is_superuser:
        profile, created = Profile.objects.get_or_create(user=self)
        self._profile_cache = profile
        return profile

    return None

# Attach the get_profile method to the User model
User.add_to_class("get_profile", get_profile)
