from django.urls import path
from . import views
app_name = 'djangoFormApp'
urlpatterns = [
    path('', views.product_form_view, name='index'),
]