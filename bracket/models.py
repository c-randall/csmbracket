from django.db import models
import datetime

# Create your models here.

class Entry(models.Model):
    name = models.CharField(max_length=50)

    participating = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True)

    series1 = models.CharField(max_length=12)
    series2 = models.CharField(max_length=12)
    series3 = models.CharField(max_length=12)
    series4 = models.CharField(max_length=12)
    series5 = models.CharField(max_length=12)
    series6 = models.CharField(max_length=12)
    series7 = models.CharField(max_length=12)
    series8 = models.CharField(max_length=12)
    series9 = models.CharField(max_length=12)
    series10 = models.CharField(max_length=12)
    series11 = models.CharField(max_length=12)
    series12 = models.CharField(max_length=12)
    series13 = models.CharField(max_length=12)
    series14 = models.CharField(max_length=12)
    series15 = models.CharField(max_length=12)

    points = models.PositiveSmallIntegerField(default=0)
    tpp = models.PositiveSmallIntegerField(default=380)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.name

class Series(models.Model):
    num = models.PositiveSmallIntegerField()

    IsComplete = models.BooleanField(default=False)

    Away = models.CharField(max_length=12, blank=True)
    Home = models.CharField(max_length=12, blank=True)

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

    class Meta:
        ordering = ('num',)
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def __str__(self):
        return str(self.num)

class MasterBracket(models.Model):
    series1 = models.CharField(max_length=12, blank=True)
    series2 = models.CharField(max_length=12, blank=True)
    series3 = models.CharField(max_length=12, blank=True)
    series4 = models.CharField(max_length=12, blank=True)
    series5 = models.CharField(max_length=12, blank=True)
    series6 = models.CharField(max_length=12, blank=True)
    series7 = models.CharField(max_length=12, blank=True)
    series8 = models.CharField(max_length=12, blank=True)
    series9 = models.CharField(max_length=12, blank=True)
    series10 = models.CharField(max_length=12, blank=True)
    series11 = models.CharField(max_length=12, blank=True)
    series12 = models.CharField(max_length=12, blank=True)
    series13 = models.CharField(max_length=12, blank=True)
    series14 = models.CharField(max_length=12, blank=True)
    series15 = models.CharField(max_length=12, blank=True)

    points = models.PositiveSmallIntegerField(default=0)
    tpp = models.PositiveSmallIntegerField(default=380)

    class Meta:
        verbose_name = "Master"
        verbose_name_plural = "Master"

    def __str__(self):
        return 'master'

class StartingTeam(models.Model):
    Index = models.PositiveSmallIntegerField()
    Name = models.CharField(max_length=12)

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
    ResetAll = models.BooleanField(default=False)
    UpdateAll = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Admin Control'
        verbose_name_plural = 'Admin Controls'

    def __str__(self):
        return 'controlform'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(null=True, default=datetime.datetime.now())
    message = models.TextField()
    image = models.ImageField(upload_to='bracket/static/images/BlogPosts', blank=True)
    embedlink = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

class RoundDates(models.Model):
    Round1 = models.CharField(max_length=20)
    Round2 = models.CharField(max_length=20)
    Round3 = models.CharField(max_length=20)
    Round4 = models.CharField(max_length=20)

    def __str__(self):
        return 'rounddates'
