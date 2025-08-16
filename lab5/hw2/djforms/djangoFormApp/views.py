from django.shortcuts import render
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    in_stock = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),initial=True)
   
def product_form_view(request):
    
    form = ProductForm()
    return render(request, 'djangoForm.html', {'form': form})

# Create your views here.
