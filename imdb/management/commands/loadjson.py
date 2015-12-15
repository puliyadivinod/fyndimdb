from django.core.management.base import BaseCommand
from optparse import make_option
import logging
import sys
import json
from imdb.models import (ImdbDirector, ImdbGenreCategory,
                         ImdbMovie, ImdbMovieGenres)
import os

__author__ = 'vinu'


class Command(BaseCommand):
    help = """Load json Data, use -h option for parameters help."""

    option_list = BaseCommand.option_list + (
        make_option('-f', '--file', type='string',
                    help='specify json file path to be processed.'),
    )

    def handle(self, *args, **options):
        if options['file'] is None:
            logging.warn("File is required input.")
            sys.exit()

        data_file = options['file']

        if os.path.exists(data_file):
            file_to_json = json.loads(open(data_file, "r").read())

            ImdbDirector.objects.all().delete()
            ImdbGenreCategory.objects.all().delete()
            ImdbMovie.objects.all().delete()
            ImdbMovieGenres.objects.all().delete()

            for record in file_to_json:
                director_name = record.get("director")
                dir_obj, dir_created = ImdbDirector.objects.get_or_create(name=director_name)

                genres_objs = []
                genres = record.get("genre")
                for genre in genres:
                    genre = genre.strip()
                    genre_obj, genre_category_created = ImdbGenreCategory.objects.get_or_create(name=genre)
                    genres_objs.append(genre_obj)

                movie_name = record.get("director")
                movie_name = record.get("director")
                movie_name = record.get("director")

                movie_data = {
                    "name": record.get("name"),
                    "director": dir_obj,
                    "number_99popularity": record.get("99popularity"),
                    "imdb_score": record.get("imdb_score")
                }

                movie_obj, movie_created = ImdbMovie.objects.get_or_create(**movie_data)

                movie_genres = []
                for gobj in genres_objs:
                    movie_genres.append(ImdbMovieGenres(movie=movie_obj, genre=gobj))

                ImdbMovieGenres.objects.bulk_create(movie_genres)







