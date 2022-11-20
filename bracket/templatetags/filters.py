# coding=utf-8
from django.template import Library

register = Library()

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
