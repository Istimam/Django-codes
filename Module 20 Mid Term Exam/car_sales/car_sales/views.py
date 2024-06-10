from django.shortcuts import render, redirect
from cars.models import Car
from brands.models import CarBrand
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from cars.models import Car, Purchase
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
        context['purchased_cars'] = Purchase.objects.filter(user=self.request.user)
        return context
    
@login_required
def buy_now(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        # Add the car to the user's purchase list
        Purchase.objects.create(user=request.user, car=car)
        messages.add_message(request, messages.SUCCESS, 'Car purchased successfully!')
    else:
        messages.add_message(request, messages.WARNING, 'This car is out of stock.')
    return redirect('car_details', pk=pk)