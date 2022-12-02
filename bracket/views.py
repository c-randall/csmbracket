from django.shortcuts import render
from django.contrib import messages
from .models import Entry, Series, StartingTeam, AdminControl, BlogPost
from .forms import EntryForm
from .utils import *
from PIL import Image

import os
import datetime
import numpy as np
import pandas as pd

# Create your views here.
def index(request):

    blogquery = BlogPost.objects.all().order_by('-date')
    context = {'blogposts': blogquery}

    return render(request, 'index.html', context)

def masterpage(request):

    seriesquery = Series.objects.all().order_by('num')
    series_list = [series.num for series in seriesquery]

    if any(series >= 1 for series in series_list):
        round1 = seriesquery.filter(num__lte=8)
    else:
        round1 = False

    if any(series >= 9 for series in series_list):
        round2 = seriesquery.filter(num__gte=9, num__lte=12)
    else:
        round2 = False

    if any(series >= 12 for series in series_list):
        round3 = seriesquery.filter(num__gte=13, num__lte=14)
    else:
        round3 = False

    if any(series >= 15 for series in series_list):
        round4 = seriesquery.filter(num__gte=15)
    else:
        round4 = False

    context = {'round1': round1, 'round2': round2, 'round3': round3, 'round4': round4}
    return render(request, 'bracket/master.html', context)

def standingspage(request, show_img, sort):

    scores = np.array([10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 50, 50, 100])

    entryquery = Entry.objects.all()
    entriesfiltered = entryquery.filter(participating=True)

    seriescomplete = Series.objects.all().order_by('num').filter(isComplete=True)

    masterpoints = 0
    for series in seriescomplete:
        masterpoints += scores[int(series.num)-1]

    data = pd.DataFrame(columns=['Name', 'Points', 'TPP', 'img_name'])
    data.loc[len(data.index)] = ['Master', masterpoints, 380, 'MasterBracket']

    for entry in entriesfiltered:
        space = entry.name.find(' ')
        name = entry.name[0:space+2] + '.'

        data.loc[len(data.index)] = [name, entry.points, entry.tpp, entry.name.replace(' ', '_')]

    tables = {}
    tables['name'] = data.sort_values(['Name', 'Points', 'TPP'], ascending=[True,False,False])
    tables['points'] = data.sort_values(['Points', 'TPP', 'Name'], ascending=[False,False,True])
    tables['tpp'] = data.sort_values(['TPP', 'Points', 'Name'], ascending=[False,False,True])

    context = {'tables': tables, 'show_img': show_img, 'sort': sort}

    return render(request, 'bracket/standings.html', context)

def submissionpage(request):

    form_toggle = AdminControl.objects.all()[0].Form
    startingquery = StartingTeam.objects.all().order_by('Index')

    startingteams = {}
    for i,Team in enumerate(startingquery):
        startingteams[i+1] = Team.Name

    if not form_toggle:
        messages.error(request, 'Sorry, the submission form is closed...')

    def storeform(filledform):
        fields = ['name'] + ['series'+str(i+1) for i in range(15)]

        formhold = {}
        for k in fields:
            if k == 'name': formhold[k] = 'Type first and last name...'
            else: formhold[k] = ""

        if filledform:
            for k in fields:
                if filledform.cleaned_data.get(k) is not None:
                    formhold[k] = filledform.cleaned_data.get(k)

        print('\nformhold: ',formhold)

        teamclasses = {}
        for i in range(30):
            teamclasses[str(i+1)] = None

        for i in range(8):
            if formhold['series'+str(i+1)] != "":
                if formhold['series'+str(i+1)] == startingteams[2*i+1]:
                    teamclasses[str(2*i+1)] = 'winner'
                    teamclasses[str(2*i+2)] = 'loser'
                elif formhold['series'+str(i+1)] == startingteams[2*i+2]:
                    teamclasses[str(2*i+1)] = 'loser'
                    teamclasses[str(2*i+2)] = 'winner'

        for i in range(7):
            if formhold['series'+str(i+9)] != "":
                if formhold['series'+str(i+9)] == formhold['series'+str(2*i+1)]:
                    teamclasses[str(2*i+17)] = 'winner'
                    teamclasses[str(2*i+18)] = 'loser'
                elif formhold['series'+str(i+9)] == formhold['series'+str(2*i+2)]:
                    teamclasses[str(2*i+17)] = 'loser'
                    teamclasses[str(2*i+18)] = 'winner'

        return formhold, teamclasses

    formhold, teamclasses = storeform(False)

    if request.method == "POST":

        filledform = EntryForm(request.POST)

        if filledform.is_valid():
            submission = filledform.save(commit=False)

            if submission.name == 'Type first and last name...':
                formhold, teamclasses = storeform(filledform)
                messages.error(request, 'Invalid form: missing name.')

            elif ' ' not in submission.name:
                formhold, teamclasses = storeform(filledform)
                messages.error(request, 'Invalid form: need both first and last name.')

            else:
                submission.date = datetime.datetime.now()
                submission.save()
                messages.success(request, 'Submission successful!')

        else:
            formhold, teamclasses = storeform(filledform)
            messages.error(request, 'Invalid form: missing inputs.')

    print('\n',formhold,teamclasses,'\n')
    form = EntryForm(request.POST or None)
    context = {'startingteams': startingteams, 'form': form, 'formhold': formhold,
               'teamclasses': teamclasses, 'active': form_toggle}

    return render(request, 'bracket/submission.html', context)
