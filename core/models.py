from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='core_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='core_users', blank=True)
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username