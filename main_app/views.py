from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Barber, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def barbers_index(request):
   barbers = Barber.objects.all()
   return render(request, 'barbers/index.html', {
      'barbers': barbers,
   })

def barbers_detail(request, barber_id):
    barber = Barber.objects.get(id=barber_id)
    reviews = barber.reviews.all()
    
    return render(request, 'barbers/detail.html', {
        'barber': barber,
        'reviews': reviews
    })
class BarberCreate(CreateView):
    model = Barber
    fields = ('name', 'phone', 'bio', )

class BarberUpdate(UpdateView):
   model = Barber
   fields = ('phone', 'bio')

class BarberDelete(DeleteView):
   model = Barber
   success_url = '/barbers'

class ReviewList(ListView):
  model = Review
   
class ReviewCreate(CreateView):
   model = Review
   fields = ('username', 'comment')

   def form_valid(self, form):
    # Set the barber instance for the review before saving
    barber = Barber.objects.get(id=self.kwargs['barber_id'])
    form.instance.barber_id = barber
    return super().form_valid(form)
   
   def form_valid(self, form):
    # Set the barber instance for the review before saving
    barber = Barber.objects.get(id=self.kwargs['barber_id'])
    form.instance.barber_id = barber
    return super().form_valid(form)
   
   

#    def form_valid(self, form):
#        # Set the barber instance for the review before saving
#        barber = Barber.objects.get(id=self.kwargs['barber_id'])
#        form.instance.barber_id = barber
#        if form.is_valid():
#            return reverse_lazy('detail', kwargs={'barber_id': barber.id})
        
        
    

#    def get_success_url(self):
#         barber_id = self.kwargs['barber_id']
#         return reverse_lazy('detail', kwargs={'barber_id': barber_id})


class ReviewUpdate(UpdateView):
    model = Review
    fields = ('comment',)


    
