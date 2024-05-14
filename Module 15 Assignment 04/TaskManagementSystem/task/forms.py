from django import forms
from . models import Task
from category.models import Category
class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = Task
        fields = '__all__'