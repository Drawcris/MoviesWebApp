"""
URL configuration for MoviesWebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from MoviesWeb.views import all_movies, create_movie, update_movie, delete_movie

urlpatterns = [
       path('all/', all_movies, name='all_movies'),
       path('create/', create_movie, name='create_movie'),
       path('update/<int:id>', update_movie, name='update_movie'),
       path('delete/<int:id>', delete_movie, name='delete_movie'),
]
