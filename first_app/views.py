from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index(request):
    # return HttpResponse('Hello world !')
    my_dict = {'insert_me': 'hello I am from views.py', 'insert_me2': 'hello I am from views.py2'}
    return render(request, "first_app/index.html", context=my_dict)
