from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    image = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
        default='profile_pictures/default-profile-photo.png')
    birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Party(models.Model):
    title = models.CharField(max_length=100)
    partyImage = models.ImageField(
        upload_to='party_pictures',
        blank=True,
        null=True,
        default='party_pictures/default-party-photo.jpg')
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()
    maxPpl = models.PositiveSmallIntegerField(blank=True, null=True)
    minAge = models.PositiveSmallIntegerField(blank=True, null=True)
    maxAge = models.PositiveSmallIntegerField(blank=True, null=True)
    targetSex = models.CharField(max_length=20, blank=True, null=True)
    owner = models.ForeignKey(Profile, related_name='parties')

    def __unicode__(self):
        return u"{}".format(self.title)