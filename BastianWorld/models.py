#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    left = models.BooleanField()
    right = models.BooleanField()
    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title

class AlbumImage(models.Model):
    # Zaktualizuj import
    from pilkit.processors import ResizeToFill
    photo = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(1280, 1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(300, 300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

class Services(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to='albums', blank=True, null=True)
    left = models.BooleanField()
    right = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Qualifications(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    photo = models.ImageField(upload_to='images/')
    left = models.BooleanField()
    right = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contakt(models.Model):
    Nazwa = models.CharField(max_length=70,blank=True, null=True)
    NrTel = models.CharField(max_length=70,blank=True, null=True)
    EMail = models.CharField(max_length=70,blank=True, null=True)
    GitHub = models.CharField(max_length=200,blank=True, null=True)
    LinkedIn = models.CharField(max_length=200,blank=True, null=True)
    Facebook = models.CharField(max_length=200,blank=True, null=True)


class Start(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)