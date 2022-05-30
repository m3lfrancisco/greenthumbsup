import os, uuid, boto3
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Plant, Fertilizer, Photo
from .forms import WateringForm 

import logging
logging.basicConfig(level=logging.DEBUG)

def home(request):
    """
    home view
    http://localhost:8000/
    """
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})

def about(request):
    """
    about view
    http://localhost:8000/about/
    """
    return render(request, 'about.html')

def plants_index(request):
    """
    plants index page
    http://localhost:8000/plants/
    """
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def my_plants(request):
    """
    user's plants index page
    http://localhost:8000/plants/my_plants/
    """
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/my_plants.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    """
    plant detail page
    http://localhost:8000/dogs/1/
    """
    try:
        plant = Plant.objects.get(id=plant_id)
        fertilizers_plant_doesnt_have = Fertilizer.objects.exclude(id__in = plant.fertilizers.all().values_list('id'))
        return render(request, 'plants/detail.html', {
            'plant': plant, 
            'watering_form': WateringForm,
            'fertilizers': fertilizers_plant_doesnt_have
            })
    except Plant.DoesNotExist:
        return render(request, 'errorpage.html')

class PlantCreate(LoginRequiredMixin, CreateView):
    """
    This class will create a plant object
    http://localhost:8000/plants/create/
    """
    model = Plant
    fields = ['name', 'plant_type', 'color', 'sunlight', 'adoption_date', 'notes']
    success_url = '/plants/my_plants/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    """
    This class will update a plant object from the DB
    http://localhost:8000/plants/1/update/
    """
    model = Plant
    fields = ['name', 'plant_type', 'color', 'sunlight', 'adoption_date', 'notes']
    
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id,))

class PlantDelete(LoginRequiredMixin, DeleteView):
    """
    This class will delete a plant object from the DB
    http://localhost:8000/plants/1/delete/
    """
    model = Plant
    success_url = '/plants/my_plants/'

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

@login_required
def add_photo(request, plant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except:
            print('An error occurred while uploading file to S3')
    return redirect('detail', plant_id=plant_id)

@login_required
def assoc_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
    return redirect('detail', plant_id=plant_id)

@login_required
def unassoc_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
    return redirect('detail', plant_id=plant_id)

def signup(request):
    """
    signup page
    http://localhost:8000/accounts/signup/
    """
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up, please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class FertilizerList(LoginRequiredMixin, ListView):
    """
    fertilizer index page
    http://localhost:8000/fertilizers/
    """
    model = Fertilizer

class FertilizerDetail(LoginRequiredMixin, DetailView):
    """
    fertilizer detail page
    http://localhost:8000/fertilizers/1/
    """
    model = Fertilizer

class FertilizerCreate(LoginRequiredMixin, CreateView):
    """
    This class will create a fertilizer object
    http://localhost:8000/fertilizers/create/
    """
    model = Fertilizer
    fields = '__all__'
    success_url = '/fertilizers/'

class FertilizerUpdate(LoginRequiredMixin, UpdateView):
    """
    This class will update a fertilizer object
    http://localhost:8000/fertilizers/1/update/
    """
    model = Fertilizer
    fields = '__all__'

class FertilizerDelete(LoginRequiredMixin, DeleteView):
    """
    This class will delete a fertilizer object
    http://localhost:8000/fertilizers/1/delete/
    """
    model = Fertilizer
    success_url = '/fertilizers/'