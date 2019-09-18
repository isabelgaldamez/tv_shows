from __future__ import unicode_literals
from django.db import models
from datetime import date

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Show title must have more than 2 chars'
        elif len(postData['network_name']) < 3:
            errors['network_name'] = 'Network name must be longer than 3 characters'
        elif len(postData['show_desc']) < 10:
            errors['description'] = 'Show description should be longer than 10 chars'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()

