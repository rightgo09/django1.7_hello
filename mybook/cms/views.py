from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Book

def book_list(request):
    '''書籍の一覧'''
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html', {'books': books}, context_instance=RequestContext(request))

def book_edit(request):
    pass

def book_del(request):
    pass

