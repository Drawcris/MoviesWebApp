from django import forms
from .models import Movie, MoreInfo, Rating
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_year', 'description', 'premiere', 'imdb_rating', 'poster']
        exclude = ['comments']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wprowadź tytuł filmu',
            }),
            'director': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wprowadź imię reżysera',
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
            'director':'Reżyser',
            'release_year': 'Rok wydania',
            'description': 'Opis filmu',
            'premiere': 'Data premiery',
            'imdb_rating': 'Ocena IMDb',
            'poster': 'Plakat filmu',
        }

class MoreInfoForm(forms.ModelForm):
    class Meta:
        model = MoreInfo
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'rating_point']
        widgets = {
            'review': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Dodaj Recenzje',
        })
        }

class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Dodaj komentarz',
        }),
        label='Twój komentarz',
        max_length=500,
        required=True
    )
