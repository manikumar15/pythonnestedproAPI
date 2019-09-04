from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer,AuthorSerializer
from .models import Author,Book

#non - id based
class AuthorListView(generics.ListCreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


#id based
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

#non - id based
class BookListView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


#id based
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
