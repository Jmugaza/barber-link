from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=15)
    comment = models.TextField(max_length=250)



    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('review', kwargs={'review_id': self.id})


class Barber(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    bio = models.TextField(max_length=250)
    reviews = models.ManyToManyField('Review', related_name='barbers_reviews')


    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'barber_id': self.id})
    
