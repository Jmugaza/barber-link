from django.shortcuts import render, redirect
from .models import Barber
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')



@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
  return render(request, 'about.html')

def barbers_index(request):
   barbers = Barber.objects.all()
   return render(request, 'barbers/index.html', {
      'barbers': barbers 
   })
   