from django.views.generic import ListView
from workbook_app.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse



class BookListView(ListView):
    template_name = 'books.html'

    def get_queryset(self):
        return Book.objects.all()


class KeepOrDeleteView(View):

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.marked_for_deletion = not book.marked_for_deletion
        book.save()

        url = reverse('workbook_app:books')
        return HttpResponseRedirect(url)
