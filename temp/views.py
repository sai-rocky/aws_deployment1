from django.shortcuts import render

def home(request):
    return render(request, 'temp/home.html')

def about(request):
    return render(request, 'temp/about.html')