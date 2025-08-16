from django.urls import path
from . import views

app_name = 'modelFormApp'

urlpatterns = [
    path('', views.product_form_view, name='index'),
    # ...existing code...
]