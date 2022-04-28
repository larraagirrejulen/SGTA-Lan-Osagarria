from django.db import models


class Book(models.Model):
    isbn = models.IntegerField()
    izena = models.CharField(max_length=60)

    def __unicode__(self):
        return self.izena