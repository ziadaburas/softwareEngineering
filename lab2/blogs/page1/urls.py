from django.urls import path
from .views import hello_app

urlpatterns = [
    path('', hello_app, name='hello_app'),
]
