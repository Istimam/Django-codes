from django.shortcuts import render, redirect
from cars.models import Car
from brands.models import CarBrand
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
def home(request):
    model = request.GET.get('model')
    if model:
        data = Car.objects.filter(brand__name=model)
    else:
        data = Car.objects.all()
    
    cars = CarBrand.objects.all()
    brand_counts = {car_brand.name: Car.objects.filter(brand = car_brand).count()
                    for car_brand in cars
                    }
    context = {
        'data': data,
        'cars': cars,
        'brand_counts': brand_counts,
    }
    return render(request, 'home.html', context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'
    redirect_field_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchased_cars'] = self.request.user.bought_cars.all()
        return context