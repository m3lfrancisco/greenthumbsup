from django.forms import ModelForm
from .models import Watering, Fertilizer

class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date', 'time', 'frequency']

class FertilizingForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['fert_date', 'frequency']