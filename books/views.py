from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView
# Create your views here.

class BookListView(ListView):
    model = Book
    contect_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Manager').exists()

class BookCreateView(ManagerRequiredMixin,CreateView):
    model = Book
    fields = ('title', 'author', 'price', 'date_publication', 'cover')
    template_name = 'books/book_new.html'