from django.contrib import admin
from .models import Barber, Review

# Register your models here.
admin.site.register([Barber, Review])
