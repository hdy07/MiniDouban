from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404
# Create your views here.
def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__contains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, 'bookhome.html', {'searchTerm':searchTerm, 'books':books})
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookdetail.html', {'book': book})