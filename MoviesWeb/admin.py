from django.contrib import admin
from .models import Movie, MoreInfo, Rating, Cast

# Register your models here.
# admin.site.register(Movie)

@admin.register(Movie)
class FilmAdmin(admin.ModelAdmin):
   # fields = ['title', 'description', 'release_year']
   # exclude = ['premiere']
    list_display = ['title', 'release_year', 'imdb_rating']
    list_filter = ['release_year']
    search_fields = ['title', 'description']



admin.site.register(MoreInfo)
admin.site.register(Rating)
admin.site.register(Cast)
