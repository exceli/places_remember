from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('address', 'title', 'review',)
        widgets = {
            # 'address': forms.HiddenInput,
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'review': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }

