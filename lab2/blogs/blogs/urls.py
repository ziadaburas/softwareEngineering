"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h2>Pages</h2><ul>'
        '<li><a href="/page1/">Page 1</a></li>'
        '<li><a href="/page2/">Page 2</a></li>'
        '<li><a href="/page3/">Page 3</a></li>'
        '</ul>'
        ''')

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('page1/', include('page1.urls')),
    path('page2/', include('page2.urls')),
    path('page3/', include('page3.urls')),
]
