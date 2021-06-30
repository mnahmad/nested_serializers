from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    # since we are in a hurry so avoiding usualy methods


class BookDetails(models.Model):
    bok = models.ForeignKey('Book', on_delete=models.CASCADE,related_name="rbook")
    summary = models.CharField(max_length=200)


