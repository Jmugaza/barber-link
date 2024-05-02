from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Barber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    bio = models.TextField(max_length=250)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'barber_id': self.id})
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    barber_id = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='reviews')
    

    def __str__(self):
        return self.user
    
    def get_absolute_url(self):
        return reverse('reviews_index') + f'#{self.pk}'
