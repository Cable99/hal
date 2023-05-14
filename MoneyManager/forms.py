from django import forms
from .models import movimenti
from django.contrib.auth import authenticate, login
from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from django.forms.widgets import DateInput, RadioSelect, Select


class MovimentiForm(forms.ModelForm):
    class Meta:
        TYPE = [('+', '+'), ('-', '-')]
        TYPE_DESCRIZIONE = [
            ('  ', '  .... '),
            ('Colazione', 'Colazione'),
            ('Pranzo', 'Pranzo'),
            ('Cena', 'Cena'),
            ('Spesa', 'Spesa'),
            ('Biglietto Treno', 'Biglietto Treno'),
            ('Biglietto Aereo', 'Biglietto Aereo'),
            ('Spesa', ' Spesa'),
            ('Cinema', 'Cinema'),
            ('Altro', 'Altro...'),
        ]
        user_id =  ['user']
        data = forms.DateField()
        descrizione = forms.CharField(max_length=20)
        tipologia = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE)
        cifra = forms.FloatField()

        model = movimenti
        fields = ['data', 'descrizione', 'tipologia', 'cifra', 'nome_icona']

        widgets = {
            'data' : DateInput(attrs={'type':'date'}),
            #'descrizione' : forms.Select(choices=TYPE_DESCRIZIONE, attrs={'class':'form-select'}),
            'tipologia' : forms.RadioSelect(choices=TYPE, attrs={'type':'radio'}),
        }
