from django import forms
from .models import Dictionary

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields =['word','part_of_speech','description']


class DictionaryForm2(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['word', 'part_of_speech', 'description']