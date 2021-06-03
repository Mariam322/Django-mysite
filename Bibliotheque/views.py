from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from Bibliotheque.models import Book, Author, BookInstance, Genre
from django.views import generic






def index7(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, "vit.html", context=context)

# class BookListView(generic.ListView):
#     model = Book
#     def get_queryset(self):
#         return Book.objects.filter(title__icontains='war')[:5]
#     def get_context_data(self, **kwargs):
#         context = super(BookListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context
def livres(request):
    context = {}
    return render(request, 'livres.html', context)
def contact(request):
    context = {}
    return render(request, 'contactus.html', context)
def cont(request):
    context = {}
    return render(request, 'cont.html', context)

