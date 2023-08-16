from django.db import models

# Create your models here.


class Contact(models.Model):
    MAX_LENGTH_NAME = 30
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    number = models.IntegerField()
