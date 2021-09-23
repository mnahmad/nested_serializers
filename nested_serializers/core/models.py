from django.db import models

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
    
