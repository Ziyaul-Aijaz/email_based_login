from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # add additional fields in here
    address = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)

    
    def __str__(self):
        return self.email