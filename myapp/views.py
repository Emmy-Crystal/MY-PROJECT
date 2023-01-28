from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import feature

def index(request):
    feature1= feature()
    feature1.name = 'Crystal Blog'
    feature1.id = 0
    feature1.details = 'Welcome to this blog. Blog what is blogable'
    
    return render(request, 'index.html', {'feature': feature1})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html', {'amount': amount_of_words})