from django import forms
from .models import Comments, Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'name', 'description', 'image', 'price', 'quantity']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'comment']