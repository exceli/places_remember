from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('address', 'title', 'review',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 60, 'rows': 5,
            }),
        }