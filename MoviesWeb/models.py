from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    release_year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(blank=True, default="")
    premiere = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    poster = models.ImageField(upload_to='movieposters', null = True, blank=True)

    def __str__(self):
        return self.title_with_a_year()

    def title_with_a_year(self):
        return "{} ({})".format(self.title, self.release_year)
