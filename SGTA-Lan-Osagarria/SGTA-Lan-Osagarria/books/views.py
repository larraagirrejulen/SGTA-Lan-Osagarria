from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
#from lxml import etree

def index(request):
    izena = 1
    id=1232
    b1 = Book(id,123,izena)
    b1.save()
    return HttpResponse("Hola!")