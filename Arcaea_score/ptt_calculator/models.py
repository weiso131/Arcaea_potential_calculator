from django.db import models
from django.contrib.auth.models import User


PST = "Past"
PRS = "Present"
FTR = "Future"
ETR = "Eternal"
BYD = "Beyond"
MOM = "Moment"
ETE = "Eternity"

class Song(models.Model):
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=120)
    def __str__(self):
        return f"{self.title}"

class Difficulty(models.Model):
    
    LEVEL_CHOICES = [
        (PST, "PST"),
        (PRS, "PRS"),
        (FTR, "FTR"),
        (ETR, "ETR"),
        (BYD, "BYD"),
        (MOM, "MOM"),
        (ETE, "ETE"),
    ]
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    note = models.IntegerField()
    chart_constant = models.FloatField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)





