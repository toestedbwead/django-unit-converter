from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .forms import LengthForm
from .conversion import convert_length

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
class WeightView(TemplateView):
    template_name = 'converter/weight.html'

# temperature view
class TemperatureView(TemplateView):
    template_name = 'converter/temperature.html'