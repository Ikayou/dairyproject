from django.forms import ModelForm
from .models import Page
from django import forms

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'page_date', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content', 'rows': 5}),
            'page_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }