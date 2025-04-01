from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['premiere'] Jak coś nie chcemy