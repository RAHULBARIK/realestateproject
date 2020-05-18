from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    # message is a optional attribute so settings blank is equal to true
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # datetimefield is field that signifies datetime of a object now the default= datetime.now will set the current timing of the contact posted
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    # Whenever we try to print the contact attached object then it will print name of the associatd realtor name
# Create your models here.
