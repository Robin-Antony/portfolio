from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(max_length=400)

    def __str__(self):
        return self.email

class Project(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

        
class Photo(models.Model):
    photo = models.ImageField()

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
