from django import forms

from .models import Feed


class FeedForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Feed title',
            }
        )
    )
    url = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Feed url',
            }
        )
    )

    class Meta:
        model = Feed
        fields = [
            'title',
            'url'
        ]
