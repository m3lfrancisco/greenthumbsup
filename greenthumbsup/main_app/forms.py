from django import forms
from django.forms import ModelForm
from .models import Watering, Fertilizer

class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date', 'time', 'frequency']

class FertilizingForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['fertilize_date', 'frequency']

def get_fert_choices():
    return [(obj.Option_Name,obj.Option_Name) for obj in Fertilizer.objects.values_list('Option_Name',flat=True).distinct()]

class FertAndServiceForm(forms.ModelForm):
    fertserv = forms.ChoiceField(choices=get_fert_choices)

    class Meta:
        model = FertAndService
        fields = [
            'fertserv', 'name', 'frequency'
        ]

# John's assist
def get_fertilizers():
    allFerts = Fertilizer.objects.all()
    fertList = list(allFerts)
    fertilizers = ()
    for f in fertList:
        fertilizers.append(f.name)

    return fertilizers