from django import forms
from .models import CarMake, CarModel, Review

class CarMakeForm(forms.ModelForm):
    
    class Meta:
        model=CarMake
        fields='__all__'

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model=CarModel
        fields='__all__'