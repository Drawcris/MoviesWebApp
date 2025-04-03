from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextField


# Create your models here.
class MoreInfo(models.Model):
    GENRE = {
        (0, 'Inne'),
        (1, 'Dramat'),
        (2, 'Komedia'),
        (3, 'Horror'),
        (4, 'Sci-Fi'),
        (5, 'Akcja'),
        (6, 'Fantasy'),
    }

    running_time = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)

    def __str__(self):
        return self.get_genre_display() + str(self.running_time)

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    release_year = models.PositiveSmallIntegerField(default=2000)
    director = models.CharField(max_length=32, blank=True, default="")
    description = models.TextField(blank=True, default="")
    premiere = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    poster = models.ImageField(upload_to='movieposters', null = True, blank=True)
    more_info = models.OneToOneField(MoreInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_with_a_year()

    def title_with_a_year(self):
        return "{} ({})".format(self.title, self.release_year)

class Rating(models.Model):
    review = TextField(default="",blank=True)
    rating_point = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.rating_point}"

class Cast(models.Model):
    full_name = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie, related_name="actors")

    def __str__(self):
        return f"{self.full_name}"