from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.sites.urls),
    path('', views.home, name='home'),
    path('add', views.add, name='add')
]