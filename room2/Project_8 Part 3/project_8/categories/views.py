from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully')
            return redirect('add_category')
    else:
        form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form': form})