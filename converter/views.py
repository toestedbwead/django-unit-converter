from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .forms import LengthForm
from .conversion import convert_length
from .forms import WeightForm
from .conversion import convert_weight
from .forms import TemperatureForm
from .conversion import convert_temperature

# home view
class HomeView(TemplateView):
    template_name = 'converter/home.html'

# length view
class LengthView(View):
    def get(self, request):
        form = LengthForm()
        return render(request, 'converter/length.html', {'form': form})
    
    def post(self, request):
        form = LengthForm(request.POST)
        
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            result = convert_length(value, from_unit, to_unit)

            context = {
                'form': form,
                'result': result,
                'value': value,
                'from_unit': from_unit,
                'to_unit': to_unit,
            }

            return render(request, 'converter/length.html', context)
        
        else:
            return render(request, 'converter/length.html', {'form': form})
        
# weight view
class WeightView(View):
    def get(self, request):
        form = WeightForm()
        return render(request, 'converter/weight.html', {'form': form})
    
    def post(self, request):
        form = WeightForm(request.POST)

        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            result = convert_weight(value, from_unit, to_unit)

            context = {
                'form': form,
                'result': result,
                'value': value,
                'from_unit': from_unit,
                'to_unit': to_unit,
            }

            return render(request, 'converter/weight.html', context)
        
        else:
            return render(request, 'converter/weight.html', {'form': form})

# temperature view
class TemperatureView(View):
    def get(self, request):
        form = TemperatureForm()
        return render(request, 'converter/temperature.html', {'form': form})
    
    def post(self, request):
        form = TemperatureForm(request.POST)

        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            result = convert_temperature(value, from_unit, to_unit)

            context = {
                'form': form,
                'result': result,
                'value': value,
                'from_unit': from_unit,
                'to_unit': to_unit,
            }

            return render(request, 'converter/temperature.html', context)
        
        else:
            return render(request, 'converter/temperature.html', {'form': form})
