from django.shortcuts import render
from .forms import ProductForm

def product_form_view(request):
    
    form = ProductForm()
    return render(request, 'modelForm.html', {'form': form})

# Create your views here.
