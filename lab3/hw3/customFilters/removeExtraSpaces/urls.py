# from django.urls import path
from .views import example_view


# urlpatterns = [
#     path('', example_view, name='example'),
# ]

from django.urls import path

urlpatterns = [
    path('', example_view, name='example'),
    # path('', hello_app, name='hello_app'),
    
]
