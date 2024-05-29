from django import forms
from .models import Entry

## Create Form

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'comment', 'rate']