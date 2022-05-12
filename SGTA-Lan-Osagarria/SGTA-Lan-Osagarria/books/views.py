from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.core import serializers
import xml.etree.cElementTree as ET
#from lxml import etree

def index(request):

    book_list=Book.objects.all()
    root = ET.Element("bib")
    for b in book_list:
        book=ET.SubElement(root,"book",year=b.year)
        ET.SubElement(book,"title").text=b.title
        author=ET.SubElement(book,"author")
        ET.SubElement(author,"last").text=b.last
        ET.SubElement(author,"first").text=b.first
        ET.SubElement(book,"publisher").text=b.publisher
        ET.SubElement(book,"price").text=str(b.price)
    tree=ET.ElementTree(root)
    tree.write("file.xml")

    #id=1
    #book="abcd"
    #year="1994"
    #title="a"
    #author="a"
    #last="a"
    #first="a"
    #editor="a"
    ##affiliation=models.CharField(max_length=255)
    #publisher="a"
    #price=12
    #b1=Book(id,book,year,title,author,last,first,editor,publisher,price)
    #b1.save()
    return render(request, 'books/index.html')
    #return HttpResponse("Hola!")

def liburuakIkusi(request):
    book_list=Book.objects.all()
    return render(request, 'books/liburuakIkusi.html',{"liburuak":book_list})

def liburuakSortu(request):
    return render(request, 'books/liburuakSortu.html')

