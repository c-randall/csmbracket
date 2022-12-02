from django.contrib import admin
from .models import Entry, Series, StartingTeam, AdminControl, BlogPost

from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'participating', 'date')
    list_editable = ('participating',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PositiveSmallIntegerField: {'widget': TextInput(attrs={'size':'1'})}
    }

    base_list = ('num', 'Away', 'Home')
    game_list = tuple()
    for i in range(7):
        game_list = game_list + tuple(['AwayG'+str(i+1)])
        game_list = game_list + tuple(['HomeG'+str(i+1)])

    list_display =  base_list + game_list
    list_editable = game_list

@admin.register(StartingTeam)
class StartingTeamsAdmin(admin.ModelAdmin):
    list_display = ('Index', 'IsEliminated', 'Name', 'DivisionRank', 'RegSeasonRank')

@admin.register(AdminControl)
class AdminPageControl(admin.ModelAdmin):
    list_display = ('AdminOnly', 'SeriesTracker', 'Form', 'UpdateAll',)
    list_editable = ('Form', 'UpdateAll',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date',)
