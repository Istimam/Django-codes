from django.shortcuts import render, redirect
from .forms import BrandForm# Create your views here.
def add_brand(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BrandForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect('homepage')
        else:
            form = BrandForm()
        return render(request, 'add_brand.html', {'form': form, 'title': 'Add Brand', 'button_text': 'Add Brand', 'button_class': 'btn-success'})
    else:
        return redirect('login')