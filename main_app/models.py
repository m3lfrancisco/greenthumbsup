from django.db import models
from django.urls import reverse
# from datetime import date
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

import logging
logging.basicConfig(level=logging.DEBUG)

TIME_OF_DAY_CHOICES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
# @receiver(post_save, sender=User)
# def user_profile_create(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def user_profile_save(sender, instance, **kwargs):
#     instance.profile.save()

    # def get_absolute_url(self):
    #     return reverse('user_profile', kwargs={'pk':self.id})

class Fertilizer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('fertilizers_detail', kwargs={'pk':self.id})

# class FertService(models.Model):
#     logging.info('calling FertService model')
#     fertname = models.CharField(max_length=100)
#     fertilize_date = models.DateField(null=True, blank=True)
#     frequency = models.CharField(max_length=100, blank=True)

    # def __str__(self):
    #     return f"{self.get_frequency_display()} on {self.fertilize_date}"

    # class Meta:
    #     ordering = ['-fertilize_date']

class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100)
    adoption_date = models.DateField('Adoption Date')
    notes = models.TextField(max_length=250, blank=True)
    fertilizers = models.ManyToManyField(Fertilizer, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"

class Watering(models.Model):
    date = models.DateField('Watering Date')
    time = models.CharField(
        'Time of Day',
        max_length=1,
        choices=TIME_OF_DAY_CHOICES,
        default=TIME_OF_DAY_CHOICES[0][0]
    )
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']