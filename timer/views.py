# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" %now
    #return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):
    try:
       offset = int(offset) #converts the string to integer
    except ValueError:
       raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hours, it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt}) 
