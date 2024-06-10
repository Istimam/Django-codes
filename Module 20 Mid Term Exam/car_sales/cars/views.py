from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Car, Comments
from .forms import CommentsForm
from .models import Car, Purchase
from django.contrib import messages

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comments_form = CommentsForm(data=self.request.POST)
        car = self.get_object()
        if comments_form.is_valid():
            new_comment = comments_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('car_details', pk=car.pk)
        return self.get(self, request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.object.brand
        brand_cars_count = Car.objects.filter(brand=brand).count()
        car = self.object
        comments = car.comments.all()
        comments_form = CommentsForm()

        context['brand_cars_count'] = brand_cars_count
        context['comments'] = comments
        context['comments_form'] = comments_form
        return context


