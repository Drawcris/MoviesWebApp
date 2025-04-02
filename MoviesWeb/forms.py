from django import forms
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wprowadź tytuł filmu',
            }),
            'release_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rok wydania (np. 2023)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dodaj krótki opis filmu...',
                'rows': 3,
            }),
            'premiere': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data premiery (YYYY-MM-DD)',
                'type': 'date',
            }),
            'imdb_rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ocena IMDb (np. 8.5)',
                'step': '0.1',
                'min': 0,
                'max': 10,
            }),
            'poster': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }
        labels = {
            'title': 'Tytuł filmu',
            'release_year': 'Rok wydania',
            'description': 'Opis filmu',
            'premiere': 'Data premiery',
            'imdb_rating': 'Ocena IMDb',
            'poster': 'Plakat filmu',
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
