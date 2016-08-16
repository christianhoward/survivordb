from django.db import models

class Player(models.Model):
    pid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    occupation = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    p_url = models.CharField(max_length=50, default='noplayerimg.jpg')
    
    def __str__(self):
        name = self.firstname + " " + self.lastname
        return name

class Season(models.Model):
    sid = models.IntegerField(primary_key=True)
    seasonname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    #fsd is film start date
    fsd = models.DateField()
    #fed is film end date
    fed = models.DateField()
    #asd is air start date
    asd = models.DateField()
    #aed is air end date
    aed = models.DateField()
    players = models.ManyToManyField(Player, through='PxS')
    s_url = models.CharField(max_length=50, default='noseasonimg.jpg')
    
    def __str__(self):
        return self.seasonname
    
class PxS(models.Model):
    pid = models.ForeignKey('Player', on_delete = models.CASCADE,)
    sid = models.ForeignKey('Season', on_delete = models.CASCADE,)
    # position they finished in
    finishposition = models.IntegerField()
    # total number of players that season
    totalpositions = models.IntegerField()
    
    def __str__(self):
        name = "Player: " + str(self.pid) + " | Season: " + str(self.sid)
        return name
    
class Statistics(models.Model):
    pid = models.ForeignKey('Player', on_delete = models.CASCADE,)
    totalseasons = models.IntegerField()
    totaldays = models.IntegerField()
    tribalwins = models.IntegerField()
    individualwins = models.IntegerField()
    totalwins = models.IntegerField()
    # total votes received against the player
    totalvotesreceived = models.IntegerField()
    daysonexile = models.IntegerField()
    daysonredemption = models.IntegerField()
    # total duels won on Redemption Island
    totalduelswon = models.IntegerField()
    
    def __str__(self):
        return str(self.pid)