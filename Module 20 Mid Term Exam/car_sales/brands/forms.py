from django import forms
from django.contrib.auth.models import User
from .models import CarBrand

class BrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'