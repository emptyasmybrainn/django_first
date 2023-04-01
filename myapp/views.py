from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = "Our service is very regular"
    return render(request, 'index.html', {'feature': feature1})  #, {'name': name}

    # return HttpResponse('<h1> Hey, Welcome </h1>')
    # name = 'John'
    # context = {
    #     'name' : 'Patrick',
    #     'age' : 23,
    #     'nationality' : 'British'
    # }
    # return render(request, 'index.html', context)


def counter(request):
    # text = request.GET['text']
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})