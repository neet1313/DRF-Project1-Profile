from django.db import models

# Create your models here.


class UserProfile(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'User Profile'

    def get_full_name(self):
        """Retrieve full name of the user."""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user."""
        return self.name

    def __str__(self):
        return self.email
