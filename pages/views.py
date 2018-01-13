import json
from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail
from pages.models import Team, Player, Sponsor, Supporter
from django.core.serializers import serialize
from pages.helpers import Getter, Analyzer


def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def sponsor(request):
    return render(request, 'sponsor.html')

def support(request):
    return render(request, 'support.html')

def addSupporter(request):
    if request.method == 'POST':
        supporter_name = request.POST.get('donorName')
        player_name = request.POST.get('doneeName')
        player_first = player_name.split()[0]
        player_last = player_name.split()[1]
        try:
            player = Player.objects.filter(first_name__iexact=player_first, last_name__iexact=player_last)[0]
        except:
            player = Player.objects.filter(last_name__icontains=player_last)[0]
        Supporter.objects.create(supporter_name=supporter_name, player_name=player_name, player=player)
        print(supporter_name, player_name)  # TODO get this info into model. Ultimately need to connect to team

    return redirect('https://www.eventbrite.com/e/first-annual-de-la-salle-north-catholic-high-school-cornhole-tournament-tickets-41440379290?aff=es2')

def leaderboard(request):
    # Hit Eventbrite API endpoint for orders
    getter = Getter('events/41440379290/orders/')
    getter.get_data()

    # Parse API response
    analyzer = Analyzer()
    order_list = analyzer.get_purchases(getter.response)

    for order in order_list:
        # Get team_id for given player
        try:
            print("{} {}".format(order["first_name"], order["last_name"]))
            # Get into Team object and grab its id
            team_id = Player.objects.get(first_name__istartswith=order["first_name"][0:2], last_name__iexact=order["last_name"]).team.id
            print("Team id".format(team_id))
        except:
            print("Coundn't find matching player name")

    teams = serialize('json', Team.objects.exclude(id__in=Team.objects.filter(eventbrite_funds__isnull=True,
                                                                       corporate_funds__isnull=True)
                                                   ))
    return render(request, 'leaderboard.html', {'teams': teams})

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
    return render(request, 'opportunities.html')

def corporate_signup(request):
    return render(request, 'corporate_signup.html')

def check_promo(request):
    if request.method == "POST":
        promo_code = request.POST.get('promo_code')

        response_dict = {'company': None, 'validPromo': False, 'numTeams': 0}
        # Check promo code against what was entered in database
        if Sponsor.objects.filter(promo=promo_code).exists():
            response_dict['company'] = Sponsor.objects.get(promo=promo_code).company_name
            response_dict['validPromo'] = True
            response_dict['numTeams'] = Sponsor.objects.get(promo=promo_code).num_teams


        return HttpResponse(json.dumps(response_dict))

def register_teams(request):
    if request.method == "POST":
        # Grab the sponsoring company
        company = request.POST.get('company_name')
        print(company)

        # For each team in the post dictionary
        for i in range(len(request.POST.getlist('teamName'))):
            p1 = request.POST.getlist('p1Name')[i]
            p1_first = p1.split()[0]
            p1_last = p1.split()[1]
            p1_email = request.POST.getlist('p1Email')[i]

            p2 = request.POST.getlist('p2Name')[i]
            p2_first = p2.split()[0]
            p2_last = p2.split()[1]
            p2_email = request.POST.getlist('p2Email')[i]


            teamName = request.POST.getlist('teamName')[i]

            # Create a new team
            newTeam = Team.objects.create(name=teamName, corporate_sponsor=Sponsor.objects.get(company_name=company))
            newTeam.save()

            # Add player one to the database, connect to p2 and team
            Player.objects.create(first_name=p1_first, last_name=p1_last, email=p1_email, teammate=p2, team=newTeam)

            # Add player two to the database, connect to p1 and team
            Player.objects.create(first_name=p2_first, last_name=p2_last, email=p2_email, teammate=p1, team=newTeam)
    return render(request, 'success.html')




