from django.contrib import admin
from django.urls import path,include
from landing_page.views import home
urlpatterns = [
    path('', home, name='home'),
]
