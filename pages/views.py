from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    return render(request, 'pages/register.html')
