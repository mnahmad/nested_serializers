from django.db import models
#from datetime import datetime
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    # since we are in a hurry so avoiding usualy methods


class BookDetails(models.Model):
    bok = models.ForeignKey('Book', on_delete=models.CASCADE,related_name="rbook")
    summary = models.CharField(max_length=200)


class country(models.Model):
    #date in this modules represents time stamps
    uploaded_dte = models.DateTimeField(auto_now_add=True, null = False)
    currency = models.CharField(max_length=3)
    cntry_name = models.CharField(max_length=100)


class state(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True,null=False)
    state_name = models.CharField(max_length=100)
    country = models.ForeignKey('country', on_delete=models.CASCADE)

class town(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True,null=False)
    town_name = models.CharField(max_length=100)
    state = models.ForeignKey('state', on_delete=models.CASCADE)
    


class MyPhoto(models.Model):
    file = models.FileField(blank=False, null=False)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class Entry(models.Model):
    recorded_date = models.DateTimeField(null=False,blank=False, default=timezone.now)
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)

    def __str__(self):
        return(self.name)

class One2Many(models.Model):
    option = models.CharField(max_length=100,null=False)
    entry = models.ForeignKey(Entry,related_name='entry_One2Many', on_delete=models.CASCADE)

    def __str__(self):
        return(self.option)

class person(models.Model):
    """
    Class to hold farmer's data
        1. recorded_dte in this model represents time of data upload onto server.  

    """
    recorded_dte = models.DateTimeField(auto_now_add=True, null = False)
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length= 100, null=True)
    last_name = models.CharField(max_length= 100, null=True)
    organization = models.CharField(max_length=100,null=True) 

    def __str__(self):
        return (self.first_name)