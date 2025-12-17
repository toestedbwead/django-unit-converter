from django import forms


# format ('value_to_store', 'What_User_Sees')

LENGTH_UNITS = [
    ('millimeter', 'Millimeter'),
    ('centimeter', 'Centimeter'),
    ('meter', 'Meter'),
    ('kilometer', 'Kilometer'),
    ('inch', 'Inch'),
    ('foot', 'Foot'),
    ('yard', 'Yard'),
    ('mile', 'Mile')
]

class LengthForm(forms.Form):
    value = forms.FloatField(label='Value to Convert',
    required=True, 
    min_value = 0, 
    error_messages = {'min_value': 'Value cannot be negative.',
        'required': 'Please enter a value.',
        'invalid': 'Please enter a valid number.',
        }
    )

    from_unit = forms.ChoiceField(
        label = 'From Unit',
        choices = LENGTH_UNITS,
    )

    to_unit = forms.ChoiceField(
        label = 'To Unit',
        choices = LENGTH_UNITS,
    )


    def clean(self):
        cleaned_data = super().clean()
        from_unit = cleaned_data.get('from_unit')
        to_unit = cleaned_data.get('to_unit')

        if from_unit and to_unit and from_unit == to_unit:
            raise forms.ValidationError(
                'Cannot convert a unit to itself. Please select different units.'
            )
        
        return cleaned_data
    
WEIGHT_UNITS = [
    ('milligram', 'Milligram'),
    ('gram', 'Gram'),
    ('kilogram', 'Kilogram'),
    ('ounce', 'Ounce'),
    ('pound', 'Pound'),
]

class WeightForm(forms.Form):
    value = forms.FloatField(label='Value to Convert',
    required = True,
    min_value = 0,
    error_messages = {'min_value': 'Value cannot be negative.',
        'required': 'Please enter a value.',
        'invalid': 'Please enter a valid number.'
        }
    )

    from_unit = forms.ChoiceField(
        label = 'From Unit',
        choices = WEIGHT_UNITS,
    )

    to_unit = forms.ChoiceField(
        label = 'To Unit',
        choices = WEIGHT_UNITS,
    )

    def clean(self):
        cleaned_data = super().clean()
        from_unit = cleaned_data.get('from_unit')
        to_unit = cleaned_data.get('to_unit')

        if from_unit and to_unit and from_unit == to_unit:
            raise forms.ValidationError(
                'Cannot convert a unit to itself. Please select different units.'
            )
        
        return cleaned_data
    

TEMPERATURE_UNITS = [
    ('celsius', 'Celsius'),
    ('fahrenheit', 'Fahrenheit'),
    ('kelvin', 'Kelvin')
]

class TemperatureForm(forms.Form):
    value = forms.FloatField(label = 'Value to Convert',
    required=True,
    error_messages = {'required': 'Please enter a value.',
    'invalid': 'Please enter a valid number.'
    })

    from_unit = forms.ChoiceField(
        label = 'From Unit',
        choices = TEMPERATURE_UNITS,
    )

    to_unit = forms.ChoiceField(
        label = 'To Unit',
        choices = TEMPERATURE_UNITS
    )

    def clean(self):
        cleaned_data = super().clean()
        from_unit = cleaned_data.get('from_unit')
        to_unit = cleaned_data.get('to_unit')

        if from_unit and to_unit and from_unit == to_unit:
            raise forms.ValidationError(
                'Cannot convert a unit to itself. Please select different units.'
            )
        
        return cleaned_data