
from django import forms
from .models import *
from dynamic_forms import DynamicField, DynamicFormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .widgets import DatePickerInput, TimePickerInput


class LibraryForm(DynamicFormMixin, forms.Form):
    
    def level_choices(form):
        library = form['library'].value()
        return Level.objects.filter(library=library)
    
    def level_initial(form):
        library = form['library'].value()
        return Level.objects.filter(library=library).first()
    
    def seat_choices(form):
        return Occupied.objects.filter(level=form['level'].value())
    
    def seat_initial(form):
        level = form['level'].value()
        return Seat.objects.filter(level=level).first()
    
    library = forms.ModelChoiceField(
        queryset=Library.objects.all(),
        initial=Library.objects.all().first()
    )
    
    level = DynamicField(
        forms.ModelChoiceField,
        queryset=level_choices,
        #initial=level_initial
    )
    
    date = forms.DateField(widget=DatePickerInput)
    
    start_time = forms.TimeField(widget=TimePickerInput)
    
    end_time = forms.TimeField(widget=TimePickerInput)
    

class SeatForm(forms.Form):
    seats = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        seat_choices = kwargs.pop('seat_choices', ())
        super().__init__(*args, **kwargs)
        self.fields['seats'].choices = seat_choices
        
