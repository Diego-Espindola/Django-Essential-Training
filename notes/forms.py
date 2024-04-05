from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_title(self): # Clean and the field that we want to add a validation
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept nots about Django')
        return title
