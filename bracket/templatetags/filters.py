# coding=utf-8
from django.template import Library
from ..models import StartingTeam

register = Library()

@register.filter
def get_logo(team):
    return 'images/PNG_Files/'+team+'Circle.png'

@register.filter
def away_ft_color(series, flag):
    flag = int(flag)

    if flag == 0 and series.AwayWins == 4:
        color = StartingTeam.objects.get(Name=series.Away).TextColor

    elif flag >= 1 and flag <= 7:
        awayscore = getattr(series, 'AwayG'+str(flag))
        homescore = getattr(series, 'HomeG'+str(flag))
        if awayscore == None or homescore == None:
            color = '#000000'
        elif awayscore > homescore:
            color = StartingTeam.objects.get(Name=series.Away).TextColor
        else:
            color = '#000000'

    elif flag == 8 and series.AwayWins == 4:
        color = StartingTeam.objects.get(Name=series.Away).TextColor

    else:
        color = '#000000'

    return color

@register.filter
def away_bg_color(series, flag):
    flag = int(flag)

    if flag == 0 and series.AwayWins == 4:
        color = StartingTeam.objects.get(Name=series.Away).MainColor

    elif flag >= 1 and flag <= 7:
        awayscore = getattr(series, 'AwayG'+str(flag))
        homescore = getattr(series, 'HomeG'+str(flag))
        if awayscore == None or homescore == None:
            color = '#e1e1e1'
        elif awayscore > homescore:
            color = StartingTeam.objects.get(Name=series.Away).MainColor
        else:
            color = '#e1e1e1'

    elif flag == 8 and series.AwayWins == 4:
        color = StartingTeam.objects.get(Name=series.Away).MainColor

    else:
        color = '#e1e1e1'

    return color

@register.filter
def home_ft_color(series, flag):
    flag = int(flag)

    if flag == 0 and series.HomeWins == 4:
        color = StartingTeam.objects.get(Name=series.Home).TextColor

    elif flag >= 1 and flag <= 7:
        awayscore = getattr(series, 'AwayG'+str(flag))
        homescore = getattr(series, 'HomeG'+str(flag))
        if awayscore == None or homescore == None:
            color = '#000000'
        elif awayscore < homescore:
            color = StartingTeam.objects.get(Name=series.Home).TextColor
        else:
            color = '#000000'

    elif flag == 8 and series.HomeWins == 4:
        color = StartingTeam.objects.get(Name=series.Home).TextColor

    else:
        color = '#000000'

    return color

@register.filter
def home_bg_color(series, flag):
    flag = int(flag)

    if flag == 0 and series.HomeWins == 4:
        color = StartingTeam.objects.get(Name=series.Home).MainColor

    elif flag >= 1 and flag <= 7:
        awayscore = getattr(series, 'AwayG'+str(flag))
        homescore = getattr(series, 'HomeG'+str(flag))
        if awayscore == None or homescore == None:
            color = '#e1e1e1'
        elif awayscore < homescore:
            color = StartingTeam.objects.get(Name=series.Home).MainColor
        else:
            color = '#e1e1e1'

    elif flag == 8 and series.HomeWins == 4:
        color = StartingTeam.objects.get(Name=series.Home).MainColor

    else:
        color = '#e1e1e1'

    return color

@register.filter
def bg_color(series, flag):
    if flag == 'name_r1' and series.isComplete:
        color = StartingTeam.objects.get(Name=series.Away).MainColor
    elif flag == 'name_r2' and series.isComplete:
        color = StartingTeam.objects.get(Name=series.Home).MainColor
    else:
        color = '#e1e1e1'
    return color

@register.filter
def get_away_score(cls, game_num):
    val = getattr(cls, 'AwayG'+str(game_num))

    if val is not None: return val
    else: return ''

@register.filter
def get_home_score(cls, game_num):
    val = getattr(cls, 'HomeG'+str(game_num))

    if val is not None: return val
    else: return ''

@register.filter
def sub(val1, val2):
    return val1 - val2

@register.filter
def range_to(int1, int2):
    return range(int1, int2+1)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_1st(dictionary, key):
    return dictionary.get(2*key-1)

@register.filter
def get_2nd(dictionary, key):
    return dictionary.get(2*key)
