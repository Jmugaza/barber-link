from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .models import Barber, Review, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import boto3, uuid



@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('index')
        else:
         error_message = 'Invalid Sign Up - try again'
    form = UserCreationForm()   
    context = {'form': form, 'error_message': error_message} 
    return render(request, 'registration/signup.html', context) 



def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

@login_required
def barbers_index(request):
   barbers = Barber.objects.filter(user=request.user)
   return render(request, 'barbers/index.html', {
      'barbers': barbers
   })


@login_required
def barbers_detail(request, barber_id):
    barber = Barber.objects.get(id=barber_id)
    reviews = barber.reviews.all()
    
    return render(request, 'barbers/detail.html', {
        'barber': barber,
        'reviews': reviews
    })

import os
def add_photo(request, barber_id):
   # capture form input
    photo_file = request.FILES.get('photo-file', None)
   #check if file was provided
    if photo_file:
        # setup an s3 uploader client
        s3 = boto3.client('s3')
        # unique name for the file
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # build a url path
        url = f'{os.environ["S3_BASE_URL"]}{os.environ["S3_BUCKET"]}/{key}'
        # upload to aws
        try:
            s3.upload_fileobj(photo_file, os.environ['S3_BUCKET'], key)
            Photo.objects.create(url=url, barber_id=barber_id)
        except Exception as e:
            print('Error Uploading to s3')
            print('Exception message:', e)
    return redirect('detail', barber_id=barber_id)

class BarberCreate(LoginRequiredMixin, CreateView):
    model = Barber
    fields = ('name', 'phone', 'bio', )

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)
    


class BarberUpdate(LoginRequiredMixin, UpdateView):
   model = Barber
   fields = ('phone', 'bio')

class BarberDelete(LoginRequiredMixin, DeleteView):
   model = Barber
   success_url = '/barbers'

class ReviewList(LoginRequiredMixin, ListView):
  model = Review
   
class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('comment',)



    def form_valid(self, form):
        barber = get_object_or_404(Barber, pk=self.kwargs['barber_id'])
        form.instance.barber_id = barber
        # Set the user field to the currently logged-in user
        form.instance.user = self.request.user
        # Call the parent class's form_valid method to save the form
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ('comment',)

class ReviewDelete(DeleteView):
   model = Review
   success_url = reverse_lazy('reviews_index')


    
