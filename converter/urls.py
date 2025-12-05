from django.urls import path
from . import views

app_name = 'converter'

urlpatters = [
    path('', views.HomeView.as_view(), name='home'),
    path('length/', views.LengthView.as_view(), name='length'),
    path('weight/', views.WeightView.as_view(), name='weight'),
    path('temperature/', views.TemperatureView.as_view(), name='temperature'),
]