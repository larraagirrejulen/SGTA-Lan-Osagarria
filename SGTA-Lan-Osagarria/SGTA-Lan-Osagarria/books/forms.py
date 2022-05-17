from django import forms

from .models import Book

class BooktForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('book', 'year','title', 'author','last', 'first','editor', 'publisher','price',)
