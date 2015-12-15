
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash
from tastypie.serializers import Serializer
from django.conf.urls import url
from tastypie import fields
import json


from imdb.models import (ImdbMovieGenres, ImdbGenreCategory,
                         ImdbMovie, ImdbDirector)


class ImdbMovieGenresResource(ModelResource):
    class Meta:
        queryset = ImdbMovieGenres.objects.all()
        resource_name = 'moviegenre'
        serializer = Serializer(formats=['json', 'jsonp', ])
        always_return_data = True
        authorization = Authorization()


class ImdbGenreCategoryResource(ModelResource):
    class Meta:
        queryset = ImdbGenreCategory.objects.all()
        resource_name = 'genrecategory'
        serializer = Serializer(formats=['json', 'jsonp', ])
        always_return_data = True
        authorization = Authorization()


class ImdbDirectorResource(ModelResource):
    class Meta:
        queryset = ImdbDirector.objects.all()
        resource_name = 'director'
        serializer = Serializer(formats=['json', 'jsonp', ])
        always_return_data = True
        authorization = Authorization()

        filtering = {
            'name': ALL,
        }


class ImdbMovieResource(ModelResource):
    director = fields.ForeignKey(ImdbDirectorResource, 'director', full=True)

    class Meta:
        queryset = ImdbMovie.objects.all()
        resource_name = 'movie'
        serializer = Serializer(formats=['json', 'jsonp', ])
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()

        filtering = {
            'name': ALL,
            'director': ALL_WITH_RELATIONS,
            'created_date': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

        # authentication = ApiKeyAuthentication()
