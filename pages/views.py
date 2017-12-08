from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    return render(request, 'pages/register.html')

def donate(request):
    return render(request, 'pages/donate.html')

def leaderboard(request):
    return render(request, 'pages/leaderboard.html')