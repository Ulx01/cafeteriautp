from django import forms

class NameForm(forms.Form):
    text_suggestion = forms.CharField(label='text_suggestion', max_length=500)