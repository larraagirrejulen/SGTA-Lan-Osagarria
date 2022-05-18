from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.core import serializers
from django.contrib import messages
import xml.etree.cElementTree as ET


#from lxml import etree

def xmlEguneratu():
    book_list=Book.objects.all()
    root = ET.Element("bib")
    for b in book_list:
        book=ET.SubElement(root,"book",year=b.year)
        ET.SubElement(book,"title").text=b.title
        author=ET.SubElement(book,"author")
        ET.SubElement(author,"last").text=b.last
        ET.SubElement(author,"first").text=b.first
        ET.SubElement(book,"editor").text=b.editor
        ET.SubElement(book,"publisher").text=b.publisher
        ET.SubElement(book,"price").text=str(b.price)
    tree=ET.ElementTree(root)
    tree.write("file.xml")

def index(request):

    xmlEguneratu()

    return render(request, 'books/index.html')


def liburuakIkusi(request):
    book_list=Book.objects.all()

    return render(request, 'books/liburuakIkusi.html',{"liburuak":book_list})

def liburuakSortu(request):
    
    if request.method == "POST":
        liburuak=Book.objects.all().last()
        id=liburuak.id+1
        year = request.POST.get('year')
        title = request.POST.get('title')
        last = request.POST.get('last')
        first = request.POST.get('first')
        editor = request.POST.get('editor')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')

        lib = Book(id,year,title,last,first,editor,publisher,price)
        lib.save()

        messages.success(request, "Ondo sortu da liburua da")
        xmlEguneratu()

    return render(request, 'books/liburuakSortu.html')

