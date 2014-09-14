from django.http import JsonResponse
from collections import OrderedDict
from cms.models import Book

def book_list(request):
    '''書籍と感想のJSONを返す'''
    books = []
    for book in Book.objects.all().order_by('id'):
        impressions = []
        for impression in book.impressions.order_by('id'):
            impression_dict = OrderedDict([
                ('id', impression.id),
                ('comment', impression.comment),
            ])
            impressions.append(impression_dict)

        book_dict = OrderedDict([
            ('id', book.id),
            ('name', book.name),
            ('publisher', book.publisher),
            ('page', book.page),
            ('impressions', impressions)
        ])
        books.append(book_dict)

    data = OrderedDict([ ('books', books) ])
    return JsonResponse(data)
