from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser  # Optional for built-in auth

class User(AbstractUser):  # Inherit from AbstractUser if using built-in auth
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    # Password field is included by AbstractUser if used
    groups = models.ManyToManyField('auth.Group', related_name='user_service_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_service_permissions')
 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    

