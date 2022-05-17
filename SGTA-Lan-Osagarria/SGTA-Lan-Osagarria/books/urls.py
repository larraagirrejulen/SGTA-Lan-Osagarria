from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liburuakIkusi/', views.liburuakIkusi, name='liburuakIkusi'),
    path('liburuakSortu/', views.liburuakSortu, name='liburuakSortu'),
    path('books/new', views.liburuakSortu, name='book_new')
]
