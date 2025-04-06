from django.contrib.auth.models import User
from rest_framework import serializers

from MoviesWeb.models import Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'email']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['url' ,'title', 'director', 'release_year', 'description']
