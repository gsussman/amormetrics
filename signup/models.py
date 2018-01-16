from __future__ import unicode_literals

# Create your models here.

from django.db import models
from django.utils import timezone

class EmailSignup(models.Model):
 first_name = models.CharField(max_length=25)
 last_name = models.CharField(max_length=25)
 email = models.EmailField(max_length=254)

 def __str__(self):
  return self.email
  
