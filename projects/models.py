from django.db import models

import uuid

from django.db.models.deletion import SET_NULL
from users.models import Profile
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=SET_NULL)
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )
    # owner
    Project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=40, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
