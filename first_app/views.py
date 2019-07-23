from django.shortcuts import render
from first_app.models import AccessRecord
from django.http import HttpResponse


# Create your views here.


def index(request):
    # return HttpResponse('Hello world !')
    access_records = AccessRecord.objects.order_by('date')
    data = {'objects': access_records}
    return render(request, "first_app/index.html", context=data)
