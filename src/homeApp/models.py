from sre_constants import MAX_UNTIL
from sys import maxsize
from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=222)
    Email = models.CharField(max_length=222)
    Phone= models.CharField(max_length=222)
    desc =  models.TextField()
    date = models.DateField()