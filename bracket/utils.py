from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

import os
import base64
from io import StringIO, BytesIO

from .models import Series, Entry, AdminControl, StartingTeam

# from models import Series, StartingTeam

def draw_name(bracket, name):
    bw,bh = bracket.size

    font = ImageFont.truetype('bracket/static/Stencil.ttf', size=110)

    draw = ImageDraw.Draw(bracket)
    _,_,tw,th = draw.textbbox((0,0), name, font=font)
    draw.text(((bw-tw)/2,th/2), name, align='center', font=font, fill='black')

def update_all_func(reset=False, forced=False):
    if reset == True:
        startingquery = StartingTeam.objects.all().order_by('Index')
        startingteams = [Team.Name for Team in startingquery]

        base_bracket(startingteams)

        entryquery = Entry.objects.all().filter(participating=True)
        for entry in entryquery:
            name = entry.name.replace(' ', '_')
            teams = [entry.__dict__['series'+str(i+1)] for i in range(15)]
            first_bracket(name, teams)

    AdminFlags = AdminControl.objects.all()[0]
    SeriesCount = Series.objects.all().filter(isComplete=True).count()

    if forced: AdminFlags.SeriesTracker = 0

    if AdminFlags.SeriesTracker != SeriesCount:
        scores = np.array([10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 50, 50, 100])

        entriesquery = Entry.objects.all().filter(participating=True)
        seriescomplete = Series.objects.order_by('num').filter(isComplete=True)
        seriesincomplete = Series.objects.order_by('num').filter(isComplete=False)

        for entry in entriesquery:
            choice_matrix = np.full( (15), np.nan )

            entry.points = 0
            entry.points_potential = 0
            entry.tpp = 380

            for series in seriescomplete:
                if series.Winner == getattr(entry, 'series'+str(series.num)):
                    entry.points += scores[int(series.num)-1]
                    choice_matrix[int(series.num)-1] = 1
                else:
                    choice_matrix[int(series.num)-1] = 0

            for series in seriesincomplete:
                choice_winner = getattr(entry, 'series'+str(series.num))
                if not StartingTeam.objects.get(Name=choice_winner).IsEliminated:
                    entry.points_potential += scores[int(series.num)-1]
                else:
                    choice_matrix[int(series.num)-1] = 0

            entry.tpp = entry.points + entry.points_potential
            update_entry_bracket(entry, choice_matrix)
            entry.save()

        AdminFlags.SeriesTracker = SeriesCount
        AdminFlags.save()

        update_master_bracket()

def late_entry(entry):
    name = entry.name.replace(' ', '_')
    teams = [entry.__dict__['series'+str(i+1)] for i in range(15)]
    first_bracket(name, teams)

    scores = np.array([10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 50, 50, 100])

    AdminFlags = AdminControl.objects.all()[0]

    if AdminFlags.SeriesTracker != 0:
        seriescomplete = Series.objects.order_by('num').filter(isComplete=True)
        seriesincomplete = Series.objects.order_by('num').filter(isComplete=False)

        choice_matrix = np.full( (15), np.nan )

        entry.points = 0
        entry.points_potential = 0
        entry.tpp = 380

        for series in seriescomplete:
            if series.Winner == getattr(entry, 'series'+str(series.num)):
                entry.points += scores[int(series.num)-1]
                choice_matrix[int(series.num)-1] = 1
            else:
                choice_matrix[int(series.num)-1] = 0

        for series in seriesincomplete:
            choice_winner = getattr(entry, 'series'+str(series.num))
            if not StartingTeam.objects.get(Name=choice_winner).IsEliminated:
                entry.points_potential += scores[int(series.num)-1]
            else:
                choice_matrix[int(series.num)-1] = 0

        entry.tpp = entry.points + entry.points_potential
        update_entry_bracket(entry, choice_matrix)
        entry.save()

def update_master_bracket():
    alpha = 0.5

    xvec0 = np.array([50, 50, 50, 50, 50, 50, 50, 50, 1250, 1250, 1250, 1250,
                      1250, 1250, 1250, 1250,])
    yvec0 = np.array([50, 225, 375, 550, 750, 925, 1075, 1250, 50, 225, 375,
                      550, 750, 925, 1075, 1250])

    masterbracket = Image.open('bracket/static/images/Brackets/MasterBracketInitial.png')
    redX = Image.open('bracket/static/images/PNG_Files/RedX.png')

    seriescomplete = Series.objects.all().filter(isComplete=True)

    for i,series in enumerate(seriescomplete):
        Home = Image.open('bracket/static/images/PNG_Files/'+series.Home+'Circle.png')
        Away = Image.open('bracket/static/images/PNG_Files/'+series.Away+'Circle.png')

        if series.Winner == series.Home:
            masterbracket.paste(Home, (series.XPos,series.YPos))

            GreyOut = Image.blend(Away, redX, alpha)
            loser = StartingTeam.objects.all().get(Name=series.Loser)

            if i < 8:
                ULC_XPos = xvec0[loser.Index-1]
                ULC_YPos = yvec0[loser.Index-1]

            else:
                depseries = Series.objects.all().filter(DeterminesSeries=series.num)

                if series.Loser == depseries[0].Winner:
                    ULC_XPos = depseries[0].XPos
                    ULC_YPos = depseries[0].YPos
                else:
                    ULC_XPos = depseries[1].XPos
                    ULC_YPos = depseries[1].YPos

            masterbracket.paste(GreyOut, (ULC_XPos,ULC_YPos))

        else:
            masterbracket.paste(Away, (series.XPos,series.YPos))

            GreyOut = Image.blend(Home, redX, alpha)
            loser = StartingTeam.objects.all().get(Name=series.Loser)

            if i < 8:
                ULC_XPos = xvec0[loser.Index-1]
                ULC_YPos = yvec0[loser.Index-1]

            else:
                depseries = Series.objects.all().filter(DeterminesSeries=series.num)

                if series.Loser == depseries[0].Winner:
                    ULC_XPos = depseries[0].XPos
                    ULC_YPos = depseries[0].YPos
                else:
                    ULC_XPos = depseries[1].XPos
                    ULC_YPos = depseries[1].YPos

            masterbracket.paste(GreyOut, (ULC_XPos,ULC_YPos))

        masterbracket.save('bracket/static/images/Brackets/MasterBracket.png')

def update_entry_bracket(entry, choice_matrix):

    seriesquery = Series.objects.all().order_by('num')

    name = entry.name.replace(' ', '_')
    bracket = Image.open('bracket/static/images/Brackets/'+name+'_Base.png')

    greenCir = Image.open('bracket/static/images/PNG_Files/GreenCircle.png')
    redX = Image.open('bracket/static/images/PNG_Files/RedX.png')

    for i,series in enumerate(seriesquery):
        if choice_matrix[i] == 1:
            bracket.paste(greenCir, (series.XPos-12,series.YPos-12), greenCir)

        elif choice_matrix[i] == 0:
            bracket.paste(redX, (series.XPos,series.YPos), redX)

    bracket.save('bracket/static/images/Brackets/'+name+'.png')

def base_bracket(teams):
    xvec = np.array([50, 50, 50, 50, 50, 50, 50, 50, 1250, 1250, 1250, 1250,
                     1250, 1250, 1250, 1250,])
    yvec = np.array([50, 225, 375, 550, 750, 925, 1075, 1250, 50, 225, 375,
                     550, 750, 925, 1075, 1250])

    bracket = Image.open('bracket/static/images/PNG_Files/BareBracket.png')

    for i,n in enumerate(teams):
        overlay = Image.open('bracket/static/images/PNG_Files/'+n+'Circle.png')
        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    xvec = np.array([200, 200, 200, 200, 1100, 1100, 1100, 1100, 350, 350, 950,
                     950, 500, 800, 650])
    yvec = np.array([138, 462, 838, 1162, 138, 462, 838, 1162, 300, 1000, 300,
                     1000, 650, 650, 1214])

    for i in range(15):
        overlay = Image.open('bracket/static/images/PNG_Files/Grey.png')
        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    bracket.save('bracket/static/images/Brackets/BaseBracket.png', 'PNG')

    draw_name(bracket, 'Master')
    bracket.save('bracket/static/images/Brackets/MasterBracketInitial.png', 'PNG')

def first_bracket(name, teams):
    xvec = np.array([200, 200, 200, 200, 1100, 1100, 1100, 1100, 350, 350, 950,
                     950, 500, 800, 650])

    yvec = np.array([138, 462, 838, 1162, 138, 462, 838, 1162, 300, 1000, 300,
                     1000, 650, 650, 1214])

    bracket = Image.open('bracket/static/images/Brackets/BaseBracket.png')

    bkgd = Image.new('RGBA', (100,100), (0,0,0,0))
    mask = Image.new('RGBA', (100,100), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,100,100), fill='green')

    space_ind = name.index('_')
    draw_name(bracket, name.replace('_', ' ')[:space_ind+2]+'.')

    for i,n in enumerate(teams):
        logo = Image.open('bracket/static/images/PNG_Files/'+n+'Circle.png')
        overlay = Image.composite(logo, bkgd, mask)
        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    bracket.save('bracket/static/images/Brackets/'+name+'_Base.png', 'PNG')
