from django import forms
from django.forms import widgets

from .models import Place, Images


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('address', 'title', 'review', 'images',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 60, 'rows': 5,
            }),
        }

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )


class UploadImagesForm(forms.Form):
    images = forms.FileField(widget=widgets.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Images
        fields = ('images',)