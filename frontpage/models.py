#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Age(models.Model):
    age = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.age

class Gender(models.Model):
    gender = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.gender

class Image(models.Model):
    image = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Profiletext(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    Text = models.TextField()
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    

    


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.ethnicity
        
class Education(models.Model):
    education = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.education

class Income(models.Model):
    income = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.income

class Religion(models.Model):
    religion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.religion
        
class ProfileInfo(models.Model):
    images = models.ManyToManyField(Image)
    texts = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    age = models.ManyToManyField(Age)
    gender = models.ManyToManyField(Gender)
    ethnicity = models.ManyToManyField(Ethnicity)
    education = models.ManyToManyField(Education)
    income = models.ManyToManyField(Income)
    religion = models.ManyToManyField(Religion)
    package = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name