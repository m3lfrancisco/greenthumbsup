from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIME_OF_DAY_CHOICES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Fertilizing Date')
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plants_detail', kwargs={'pk':self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100)
    adoption_date = models.DateField('Adoption Date')
    notes = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    def watered_for_today(self):
        return self.watering_set.filter(date=date.today()).count()

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