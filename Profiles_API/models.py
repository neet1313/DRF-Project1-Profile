from django.db import models

# Create your models here.


class UserProfile(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=False)
    # password = models.CharField(max_length=50, blank=False, default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def get_full_name(self):
        """Retrieve full name of the user."""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user."""
        return self.name

    def __str__(self):
        return self.email
