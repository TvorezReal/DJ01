from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    datas = {
        'title': 'EuroDjango',
    }
    return render(request, 'main/index.html', datas)

def data(request):
    return render(request, 'main/data.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')


