from django.urls import path
# make sure to import views

from . import views
urlpatterns = [
    path('',views.home, name='home')
   
]