from django.shortcuts import render, redirect
from . import forms
from . import models

from django.views.generic import DetailView
from django.contrib import messages
# Create your views here.


def add_car(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('homepage')
    else:
        form = forms.CarForm()

    return render(request, 'add_car.html', {'form': form, 'title': 'Add Car', 'button_text': 'Add Car', 'button_class': 'btn-success'})

def car_detail(request, car_id):
    car = models.Car.objects.get(id=car_id)

    if request.method == 'POST':
        if 'buy_now' in request.POST:
            if car.quantity > 0:
                car.buyers.add(request.user)
                car.quantity -= 1
                car.save()
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.error(request, 'Car is out of stock!')
        elif 'comments' in request.POST:
            comment_form = forms.CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
    comments = models.Comments.objects.filter(car=car)

    comment_form = forms.CommentForm()

    return render(request, 'car_details.html', {'car': car, 'comments': comments, 'comment_form': comment_form})
