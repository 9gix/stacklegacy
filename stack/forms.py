from django import forms
from stack.models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        exclude = ('stacks', )
