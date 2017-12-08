from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    return render(request, 'pages/register.html')

def donate(request):
    return render(request, 'pages/donate.html')

def leaderboard(request):
    return render(request, 'pages/leaderboard.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('contactName')
        message = request.POST.get('contactMsg')
        email = request.POST.get('contactEmail')
        send_mail('{} has questions'.format(name), "{} \n \n {}".format(email, message), 'dlsnc.fundraiser@gmail.com', ['jolly0313@gmail.com'],
                  fail_silently=False)
        return HttpResponse("Success")
    return HttpResponse("Message Send Failed")
