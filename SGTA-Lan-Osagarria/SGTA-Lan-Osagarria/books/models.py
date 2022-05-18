from django.db import models


class Book(models.Model):

    #book=models.CharField(max_length=255)
    year=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    last=models.CharField(max_length=255)
    first=models.CharField(max_length=255)
    editor=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    price=models.FloatField()

    def __str__(self):
        return self.title