from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name','series1','series2','series3','series4','series5','series6','series7',
        'series8','series9','series10','series11','series12','series13','series14','series15']
        widgets = {
            'series1': forms.HiddenInput(),
            'series2': forms.HiddenInput(),
            'series3': forms.HiddenInput(),
            'series4': forms.HiddenInput(),
            'series5': forms.HiddenInput(),
            'series6': forms.HiddenInput(),
            'series7': forms.HiddenInput(),
            'series8': forms.HiddenInput(),
            'series9': forms.HiddenInput(),
            'series10': forms.HiddenInput(),
            'series11': forms.HiddenInput(),
            'series12': forms.HiddenInput(),
            'series13': forms.HiddenInput(),
            'series14': forms.HiddenInput(),
            'series15': forms.HiddenInput(),
        }
