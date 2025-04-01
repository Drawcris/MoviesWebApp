from django.shortcuts import render, get_object_or_404, redirect
from django.http import response
from MoviesWeb.models import Movie
from MoviesWeb.forms import MovieForm


# Create your views here.
def all_movies(request):
    allObjectsInTable = Movie.objects.all()
    return  render(request, 'movies.html', {'movies': allObjectsInTable})

def create_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form})

def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form})

def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)


    return render(request, 'delete_confirmation.html', {'movie': movie})
