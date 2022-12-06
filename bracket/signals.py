from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

from .models import AdminControl, StartingTeam, Series, Entry, BlogPost
from .utils import *

import os
import pandas as pd
from .utils import *

@receiver(pre_save, sender=Series)
def series_dependent_fields(sender, instance, **kwargs):

    if instance.Away != '' and instance.Home != '':
        AwayTeam = StartingTeam.objects.get(Name=instance.Away)
        HomeTeam = StartingTeam.objects.get(Name=instance.Home)

        AwayScores = [instance.__dict__['AwayG'+str(i+1)] for i in range(7)]
        HomeScores = [instance.__dict__['HomeG'+str(i+1)] for i in range(7)]

        instance.AwayWins = 0
        instance.HomeWins = 0

        for i in range(7):
            if AwayScores[i] != None and HomeScores[i] != None:
                if AwayScores[i] == HomeScores[i]:
                    raise Exception('Found a tied game... input correct scores!')

                else:
                    if AwayScores[i] > HomeScores[i]: instance.AwayWins += 1
                    elif HomeScores[i] > AwayScores[i]: instance.HomeWins += 1

        if instance.AwayWins > 4 or instance.HomeWins > 4:
            raise Exception('Found more than 4 wins for a team... double check scores!')
        elif instance.AwayWins == 4 or instance.HomeWins == 4:
            instance.isComplete = True
        else:
            instance.isComplete = False
            instance.Winner = ''
            instance.Loser = ''
            HomeTeam.IsEliminated = False
            AwayTeam.IsEliminated = False
            HomeTeam.save()
            AwayTeam.save()

        if instance.isComplete:
            if instance.AwayWins == 4:
                instance.Winner = instance.Away
                instance.Loser = instance.Home
                HomeTeam.IsEliminated = True
                HomeTeam.save()
            elif instance.HomeWins == 4:
                instance.Winner = instance.Home
                instance.Loser = instance.Away
                AwayTeam.IsEliminated = True
                AwayTeam.save()

@receiver(post_save, sender=Series)
def make_matchups(sender, instance, **kwargs):

    flag = Series.objects.all().count()

    if flag == 15 and instance.DeterminesSeries != 0:

        depquery = Series.objects.order_by('num').filter(DeterminesSeries=instance.DeterminesSeries, isComplete=True)
        depcnt = depquery.count()

        series = Series.objects.get(num=instance.DeterminesSeries)

        if depcnt == 2:
            # Find winners
            upperTeam = StartingTeam.objects.get(Name=depquery[0].Winner)
            lowerTeam = StartingTeam.objects.get(Name=depquery[1].Winner)

            if instance.DeterminesSeries <= 12:
                if upperTeam.DivisionRank < lowerTeam.DivisionRank:
                    series.Home = upperTeam.Name
                    series.Away = lowerTeam.Name
                else:
                    series.Home = lowerTeam.Name
                    series.Away = upperTeam.Name

            else:
                if upperTeam.RegSeasonRank < lowerTeam.RegSeasonRank:
                    series.Home = upperTeam.Name
                    series.Away = lowerTeam.Name
                else:
                    series.Home = lowerTeam.Name
                    series.Away = upperTeam.Name

        else:
            tmpDeterminesSeries = series.DeterminesSeries
            tmpXPos, tmpYPos = series.XPos, series.YPos

            series.delete()
            series = Series(num=instance.DeterminesSeries)
            series.DeterminesSeries = tmpDeterminesSeries
            series.XPos = tmpXPos
            series.YPos = tmpYPos

        series.save()

    if flag == 15:
        update_all_func()

@receiver(pre_save, sender=AdminControl)
def admin_flags(sender, instance, **kwargs):

    if instance.Form:
        startingquery = StartingTeam.objects.all().order_by('Index')
        startingteams = [Team.Name for Team in startingquery]

        if startingquery.count() != 16:
            instance.Form = False
            raise Exception('Team count is not 16!')

    if instance.Initialize:
        startingquery = StartingTeam.objects.all().order_by('Index')
        startingteams = [Team.Name for Team in startingquery]

        base_bracket(startingteams)

        xvec = np.array([200, 200, 200, 200, 1100, 1100, 1100, 1100, 350, 350, 950,
                         950, 500, 800, 650])
        yvec = np.array([138, 462, 838, 1162, 138, 462, 838, 1162, 300, 1000, 300,
                         1000, 650, 650, 1214])

        Series.objects.all().delete()
        startingquery.update(IsEliminated=False)

        for i in range(4):
            series = Series(num=2*i+1)
            series.Home = startingteams[4*i]
            series.Away = startingteams[4*i+1]
            series.DeterminesSeries = i+9
            series.XPos = xvec[2*i]
            series.YPos = yvec[2*i]
            series.save()

            series = Series(num=2*i+2)
            series.Home = startingteams[4*i+2]
            series.Away = startingteams[4*i+3]
            series.DeterminesSeries = i+9
            series.XPos = xvec[2*i+1]
            series.YPos = yvec[2*i+1]
            series.save()

        for i in range(3):
            series = Series(num=2*i+9)
            series.DeterminesSeries = i+13
            series.XPos = xvec[2*i+8]
            series.YPos = yvec[2*i+8]
            series.save()

            series = Series(num=2*i+10)
            series.DeterminesSeries = i+13
            series.XPos = xvec[2*i+9]
            series.YPos = yvec[2*i+9]
            series.save()

        series = Series(num=15)
        series.DeterminesSeries = 0
        series.XPos = xvec[-1]
        series.YPos = yvec[-1]
        series.save()

        instance.Initialize = False
        instance.SeriesTracker = 0

        Entry.objects.all().filter(participating=True).update(points=0, points_potential=0, tpp=380)

        update_all_func(True)

    if instance.UpdateAll:
        Entry.objects.all().filter(participating=True).update(points=0, points_potential=0, tpp=380)
        instance.UpdateAll = False
        update_all_func(True, True)
        instance.SeriesTracker = Series.objects.all().filter(isComplete=True).count()

@receiver(pre_delete, sender=Entry)
def delete_bracket_files(sender, instance, **kwargs):
    name = instance.name.replace(' ', '_')

    try: os.remove('bracket/static/images/Brackets/'+name+'_Base.png')
    except: pass

    try: os.remove('bracket/static/images/Brackets/'+name+'.png')
    except: pass

@receiver(pre_delete, sender=BlogPost)
def delete_media_files(sender, instance, **kwargs):
    try: os.remove('bracket/static/'+instance.image.url)
    except: pass

@receiver(post_save, sender=Entry)
def initialize_participant(sender, instance, **kwargs):

    if instance.participating:
        name = instance.name.replace(' ', '_')
        bracket0_path = 'bracket/static/images/Brackets/'+name+'_Base.png'
        bracket1_path = 'bracket/static/images/Brackets/'+name+'.png'

        if not os.path.exists(bracket0_path) or not os.path.exists(bracket1_path):
            late_entry(instance)
