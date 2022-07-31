from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookListView(ListView):
    template_name = 'book_store/book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_store/book_detail.html'
    model = Book


class BookCreateView(CreateView):
    template_name = 'book_store/book_create.html'
    model = Book
    fields = ['title', 'description', 'author', 'category']


class BookUpdateView(UpdateView):
    template_name = 'book_store/book_update.html'
    model = Book
    fields = ['title', 'description', 'author', 'category']


class BookDeleteView(DeleteView):
    template_name = 'book_store/book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')
