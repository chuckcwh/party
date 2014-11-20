import json
import urllib
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
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    time = models.DateTimeField()
    maxPpl = models.PositiveSmallIntegerField(blank=True, null=True)
    minAge = models.PositiveSmallIntegerField(blank=True, null=True)
    maxAge = models.PositiveSmallIntegerField(blank=True, null=True)
    targetSex = models.CharField(max_length=20, blank=True, null=True)
    private = models.CharField(max_length=20)
    owner = models.ForeignKey(Profile, related_name='parties_owner')
    participants = models.ManyToManyField(Profile, related_name='parties_participants', blank=True, null=True)
    streetnum = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u"{}".format(self.title)

    def save(self, force_insert=True):
        location = "{}, {}, {}, {}".format(self.streetnum, self.street, self.city, self.country)

        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(location)

        super(Party, self).save()

    def geocode(self, location):
        location = urllib.quote_plus(location)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude