from django.db import models
import datetime

from tinymce import models as tinymce_models

# Create your models here.

class Entry(models.Model):
    name = models.CharField(max_length=50)

    participating = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True)

    series1 = models.CharField(max_length=20)
    series2 = models.CharField(max_length=20)
    series3 = models.CharField(max_length=20)
    series4 = models.CharField(max_length=20)
    series5 = models.CharField(max_length=20)
    series6 = models.CharField(max_length=20)
    series7 = models.CharField(max_length=20)
    series8 = models.CharField(max_length=20)
    series9 = models.CharField(max_length=20)
    series10 = models.CharField(max_length=20)
    series11 = models.CharField(max_length=20)
    series12 = models.CharField(max_length=20)
    series13 = models.CharField(max_length=20)
    series14 = models.CharField(max_length=20)
    series15 = models.CharField(max_length=20)

    points = models.PositiveSmallIntegerField(default=0)
    points_potential = models.PositiveSmallIntegerField(default=0)
    tpp = models.PositiveSmallIntegerField(default=380)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.name

class Series(models.Model):
    num = models.PositiveSmallIntegerField()

    Away = models.CharField(max_length=20, blank=True)
    Home = models.CharField(max_length=20, blank=True)

    AwayG1 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG1 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG2 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG2 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG3 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG3 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG4 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG4 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG5 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG5 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG6 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG6 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayG7 = models.PositiveSmallIntegerField(null=True, blank=True)
    HomeG7 = models.PositiveSmallIntegerField(null=True, blank=True)

    AwayWins = models.PositiveSmallIntegerField(default=0)
    HomeWins = models.PositiveSmallIntegerField(default=0)

    DeterminesSeries = models.PositiveSmallIntegerField(null=True, blank=True)

    isComplete = models.BooleanField(default=False)

    Winner = models.CharField(max_length=20, blank=True)
    Loser = models.CharField(max_length=20, blank=True)

    XPos = models.PositiveSmallIntegerField(default=0)
    YPos = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('num',)
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def __str__(self):
        return str(self.num)

class StartingTeam(models.Model):
    Index = models.PositiveSmallIntegerField()
    Name = models.CharField(max_length=20)

    IsEliminated = models.BooleanField(default=False)

    DivisionRank = models.PositiveSmallIntegerField()
    RegSeasonRank = models.PositiveSmallIntegerField()

    MainColor = models.CharField(max_length=7)
    TextColor = models.CharField(max_length=7)

    class Meta:
        ordering = ('Index',)

        verbose_name = 'Starting Team'
        verbose_name_plural = 'Starting Teams'

    def __str__(self):
        return self.Name

class AdminControl(models.Model):
    AdminOnly = 'Admin Controls'
    Form = models.BooleanField(default=False)
    Initialize = models.BooleanField(default=False)
    UpdateAll = models.BooleanField(default=False)
    SeriesTracker = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Admin Control'
        verbose_name_plural = 'Admin Controls'

    def __str__(self):
        return 'controlform'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(null=True, default=datetime.datetime.now())
    message = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='BlogPosts', blank=True)
    embedlink = models.CharField(max_length=3000, blank=True)

    class Meta:
        ordering = ('-date',)

        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
