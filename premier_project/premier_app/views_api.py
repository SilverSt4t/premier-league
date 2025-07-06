from django.http import JsonResponse
from .models import Match, Player

def match_data(request):
    matches = Match.objects.all().values(
        'home_team__name', 'away_team__name', 'home_score', 'away_score', 'match_date')
    return JsonResponse(list(matches), safe=False)

def top_scorers(request):
    players = Player.objects.order_by('-goals')[:10].values(
        'name', 'team__name', 'goals')
    return JsonResponse(list(players), safe=False)