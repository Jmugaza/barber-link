from django.contrib import admin
from .models import Barber, Review, Photo

# Register your models here.
admin.site.register([Barber, Review, Photo])
