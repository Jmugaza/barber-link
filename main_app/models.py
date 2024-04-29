from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Barber(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    bio = models.TextField(max_length=250)

    def __str__(self) :
        return self.name
    
