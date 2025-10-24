from django.shortcuts import render, HttpResponse 
from .models import Users

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def css_template(request):
    return render(request, 'css/style.css', content_type='text/css')