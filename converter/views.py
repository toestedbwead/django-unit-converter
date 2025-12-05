from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'converter/home.html'

class LengthView(TemplateView):
    template_name = 'converter/length.html'

class WeightView(TemplateView):
    template_name = 'converter/weight.html'

class TemperatureView(TemplateView):
    template_name = 'converter/temperature.html'