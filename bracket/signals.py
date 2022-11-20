from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import AdminControl, StartingTeam, Series, Entry
from .utils import *

import os
import pandas as pd
from .utils import *

@receiver(pre_save, sender=Series)
def make_updates(sender, instance, **kwargs):
    scores = np.array([10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 50, 50, 100])

    AwayTeam = StartingTeam.objects.get(Name=instance.Away)
    HomeTeam = StartingTeam.objects.get(Name=instance.Home)

    AwayScores = [instance.__dict__['AwayG'+str(i+1)] for i in range(7)]
    HomeScores = [instance.__dict__['HomeG'+str(i+1)] for i in range(7)]

    instance.AwayWins = 0
    instance.HomeWins = 0

    for i in range(7):
        if AwayScores[i] != None and HomeScores[i] != None:
            if AwayScores[i] > HomeScores[i]: instance.AwayWins += 1
            elif HomeScores[i] > AwayScores[i]: instance.HomeWins += 1

    if instance.AwayWins == 4:
        winner = instance.Away
        instance.IsComplete = True
        HomeTeam.IsEliminated = True
        HomeTeam.save()
    elif instance.HomeWins == 4:
        winner = instance.Home
        instance.IsComplete = True
        AwayTeam.IsEliminated = True
        AwayTeam.save()
    else:
        instance.IsComplete = False

    if instance.IsComplete:

        entryquery = Entry.objects.all()
        entriesfiltered = entryquery.filter(participating=True)

        for entry in entriesfiltered:
            if entry.__dict__['series'+str(instance.num)] == winner:
                entry.points = entry.points + scores[instance.num-1]
                entry.save()

@receiver(post_save, sender=StartingTeam)
def make_base_bracket(sender, instance, **kwargs):

    basebracket = 'bracket/static/images/Brackets/BaseBracket.png'

    startingquery = StartingTeam.objects.all().order_by('Index')
    startingteams = [Team.Name for Team in startingquery]

    if len(startingteams) < 16 and os.path.exists(basebracket):
        os.remove(basebracket)
    elif len(startingteams) == 16:
        base_bracket(startingteams)

@receiver(pre_save, sender=AdminControl)
def initialize_tournament(sender, instance, **kwargs):

    if instance.Form:
        pass
        # Check that everything needed is accessible in database,
        # otherwise turn the form back off.

    if instance.ResetAll:
        pass

    if instance.UpdateAll:
        pass

@receiver(post_save, sender=Entry)
def make_first_bracket(sender, instance, **kwargs):
    img_name = instance.name.replace(' ', '_')
    img_path = 'bracket/static/images/Brackets/'+img_name+'.png'

    if instance.participating:
        teams = [instance.__dict__['series'+str(i+1)] for i in range(15)]
        first_bracket(img_name, teams)

    elif not instance.participating and os.path.exists(img_path):
        os.remove(img_path)
