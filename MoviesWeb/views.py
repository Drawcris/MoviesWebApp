from django.shortcuts import render, get_object_or_404, redirect
from MoviesWeb.models import Movie
from MoviesWeb.forms import MovieForm, RegisterForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_movies(request):
    allObjectsInTable = Movie.objects.all()
    return  render(request, 'movies.html', {'movies': allObjectsInTable})

@login_required()
def create_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form})

@login_required()
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'create_movie.html', {'form': form})

@login_required()
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)


    return render(request, 'delete_confirmation.html', {'movie': movie})

def selected_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    comments = movie.comments.split("\n") if movie.comments else []

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Pobierz istniejące komentarze i dodaj nowy
            new_comment = form.cleaned_data['comment']
            if movie.comments:
                movie.comments += f"\n{new_comment}"  # Dodaj nowy komentarz do istniejących
            else:
                movie.comments = new_comment  # Dodaj pierwszy komentarz
            movie.save()
            # Odśwież stronę, żeby uniknąć problemów z ponownym wysyłaniem danych
            return redirect('selected_movie', id=movie.id)
    else:
        form = CommentForm()

    return render(request, 'selected_movie.html', {
        'movie': movie,
        'comments': comments,
        'form': form
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

