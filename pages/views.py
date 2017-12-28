from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail
from pages.models import Team, Player
from django.core.serializers import serialize


def home(request):
    return render(request, 'pages/home.html')

def register(request):
    return render(request, 'pages/register.html')

def sponsor(request):
    return render(request, 'pages/sponsor.html')

def support(request):
    return render(request, 'pages/support.html')

def addSupporter(request):
    if request.method == 'POST':
        supporter_name = request.POST.get('donorName')
        player_name = request.POST.get('doneeName')
        print(supporter_name, player_name)  #TODO get this info into model. Ultimately need to connect to team

    return redirect('https://www.eventbrite.com/e/first-annual-de-la-salle-north-catholic-high-school-cornhole-tournament-tickets-41440379290?aff=es2')

def leaderboard(request):
    teams = serialize('json', Team.objects.exclude(id__in=Team.objects.filter(eventbrite_funds__isnull=True,
                                                                       corporate_funds__isnull=True)
                                                   ))
    return render(request, 'pages/leaderboard.html', {'teams': teams})

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
    """Get data from registration form and push into database. Connect players to teams, where teammate known"""
    if request.method == "POST":

        # Update the players database
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        teammate = request.POST.get('teammate')

        # If teammate known at registration
        if teammate:
            # Get and split teammate name
            teammate_first = teammate.split()[0]
            teammate_last = teammate.split()[1]
            # If teammate name already in database
            if Player.objects.filter(first_name__iexact=teammate_first, last_name__iexact=teammate_last).exists():
                # Create team and give both players foreign keys to it
                newTeam = Team.objects.create()
                newTeam.save()
                Player.objects.create(first_name=first_name, last_name=last_name, email=email, teammate=teammate, team=newTeam)
                Player.objects.filter(first_name__iexact=teammate_first, last_name__iexact=teammate_last).update(teammate="{} {}".format(first_name, last_name),
                                                                                                                 team=newTeam)
            # If teammate not in database
            else:
                Player.objects.create(first_name=first_name, last_name=last_name, email=email, teammate=teammate)
        # If teammate unknown at registration
        else:
            Player.objects.create(first_name=first_name, last_name=last_name, email=email, teammate=teammate)
        return HttpResponse("You're registered!")
    else:
        return HttpResponse("Uh Oh, no data posted.")

def opportunities(request):
    return render(request, 'pages/opportunities.html')

