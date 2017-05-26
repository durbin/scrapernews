from django.db import models

class Item(models.Model):
    hnid = models.IntegerField(unique=True)
    points = models.CharField(max_length=255, blank=True, null=True)
    hacker = models.CharField(max_length=2000, blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(blank=True, null=True)


class Hacker(models.Model):
    """ 
    Not used
    """
    username = models.CharField(max_length=2000)
    karma = models.IntegerField(blank=True, null=True)
    about = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)


class Comment(models.Model):
    """ 
    Not used
    """
    text = models.CharField(max_length=2000)
    hacker = models.ForeignKey('Hacker', blank=True, null=True)
    item = models.ForeignKey('Item', blank=True, null=True)
    parent_id = models.ForeignKey('Comment', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)