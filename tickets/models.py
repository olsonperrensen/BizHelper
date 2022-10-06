from django.db import models

# Create your models here.


class Ticket(models.Model):
    mID = models.PositiveIntegerField()
    mType = models.CharField(max_length=8)
    mCreatedBy = models.CharField(max_length=80)
    mDateOfCreation = models.DateField()
    mDaysPassed = models.PositiveSmallIntegerField()
    mSolved = models.BooleanField()
    mComment = models.CharField(max_length=500)

