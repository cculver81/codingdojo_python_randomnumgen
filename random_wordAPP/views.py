from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    counter = request.session.get('counter', 0) + 1
    request.session['counter'] = counter

    context = {
        'random_string' : get_random_string(length=14),
        'counter' : counter
    }
    return render(request, 'index.html', context)

def clr_cntr(request):
    return HttpResponse('clr_cntr')