from django.shortcuts import render
from django.http import response
from MoviesWeb.models import Movie


# Create your views here.
def all_movies(request):
    allObjectsInTable = Movie.objects.all()
    return  render(request, 'movies.html', {'movies': allObjectsInTable})