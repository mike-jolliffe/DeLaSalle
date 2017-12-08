from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    return render(request, 'pages/register.html')

def donate(request):
    return render(request, 'pages/donate.html')

def leaderboard(request):
    return render(request, 'pages/leaderboard.html')


#Working email send_mail('TESTING EMAIL', 'It works, dude!', 'dlsnc.fundraiser@gmail.com', ['jolly0313@gmail.com'], fail_silently=False)