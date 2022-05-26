# from django import forms
from django.forms import ModelForm
from .models import Watering

class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date', 'time', 'frequency']

# class FertilizingForm(ModelForm):
#     class Meta:
#         model = Fertilizer
#         fields = ['fertilize_date', 'frequency']

# def get_fert_choices():
#     return [(Fertilizer.name) for obj in Fertilizer.objects.values_list('name',flat=True).distinct()]

# def get_fert_choices():
#     allFerts = Fertilizer.objects.all()
#     fertList = list(allFerts)
#     fertilizers = []
#     for f in fertList:
#         fertilizers.append(f.name)

#     return fertilizers

# class FertAndServiceForm(forms.ModelForm):
#     fertname = forms.ChoiceField(choices=get_fert_choices)

#     class Meta:
#         model = FertService
#         fields = ['fertname', 'fertilize_date', 'frequency']

# John's assist
