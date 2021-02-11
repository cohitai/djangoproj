from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.PositiveIntegerField(default=0,primary_key=True)
    url = models.CharField(max_length=200)
    title = models.TextField(blank=True)
    lead = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    publishdate = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return(str(self.id) + " " + self.title)



class BerlinerZeitung(models.Model):
    id = models.PositiveIntegerField(default=0,primary_key=True)
    url = models.CharField(max_length=200)
    title = models.TextField(blank=True)
    author =models.CharField(max_length=200) 
    publishdate = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    language = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return(str(self.id) + " : " + self.title)


