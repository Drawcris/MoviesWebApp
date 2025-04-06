from django.shortcuts import render, get_object_or_404, redirect
from MoviesWeb.models import Movie, Rating
from django.contrib.auth.models import User
from MoviesWeb.forms import MovieForm, RegisterForm, MoreInfo, MoreInfoForm, RatingForm
from django.contrib.auth.decorators import login_required
from statistics import mean
from rest_framework import viewsets
from MoviesWeb.serializers import UserSerializer, MovieSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# Create your views here.
def all_movies(request):
    allObjectsInTable = Movie.objects.all()
    return  render(request, 'movies.html', {'movies': allObjectsInTable})

@login_required()
def create_movie(request):
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_more_info = MoreInfoForm(request.POST or None)

    if form_movie.is_valid() and form_more_info.is_valid():
        film = form_movie.save(commit=False)
        more_info = form_more_info.save()
        film.more_info = more_info
        film.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form_movie, 'form_more_info': form_more_info})

@login_required()
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    try:
        more_info = MoreInfo.objects.get(movie=movie.id)
    except MoreInfo.DoesNotExist:
        more_info = None


    form_movie = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    form_more_info = MoreInfoForm(request.POST or None,  instance=more_info)

    if form_movie.is_valid() and form_more_info.is_valid():
        film = form_movie.save(commit=False)
        more_info = form_more_info.save()
        film.more_info = more_info
        film.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form_movie, 'form_more_info': form_more_info})

@login_required()
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)


    return render(request, 'delete_confirmation.html', {'movie': movie})

def get_movie_ratings(movie):
    ratings = Rating.objects.filter(movie=movie)
    list_of_ratings = [rating.rating_point for rating in ratings]
    if not list_of_ratings:
        list_of_ratings = [0]
    average_rating = mean(list_of_ratings)
    return ratings, average_rating

def handle_rating_form(request, movie):
    form = RatingForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        rating = form.save(commit=False)
        rating.movie = movie
        rating.save()
        return form, True
    return form, False

def selected_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    actors = movie.actors.filter(movies=movie)

    ratings, average_rating = get_movie_ratings(movie)

    form, form_was_submitted = handle_rating_form(request, movie)
    if form_was_submitted:
        return redirect(selected_movie, id)

    return render(request, 'selected_movie.html', {
        'movie': movie,
        'form': form,
        'ratings': ratings,
        'actors': actors,
        'average_rating': average_rating,
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

