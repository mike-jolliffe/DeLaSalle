from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from pages.models import Team, Player

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    return render(request, 'pages/register.html', {'teams': teams})

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

def add_registrant(request):
    if request.method == "POST":

        # Update the players database
        first_name = request.POST.get('txtFirstName')
        last_name = request.POST.get('txtLastName')
        email = request.POST.get('txtEmail')
        teammate = request.POST.get('pickTeammate')

        # TODO Figure out how to assign to new or existing team

        Player.objects.create(first_name=first_name, last_name=last_name, email=email, teammate=teammate)

        teammate_first = teammate.split()[0]
        teammate_last = teammate.split()[1]
        if Player.objects.filter(first_name__iexact=teammate_first, last_name__iexact=teammate_last).exists():
            print("Found!")

        return HttpResponse("You're registered!")

