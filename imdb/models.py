from django.db import models

# Create your models here.


class ImdbDirector(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'imdb_director'
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

    def __str__(self):
        return self.name


class ImdbGenreCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'imdb_genre_category'
        verbose_name = 'Genre Category'
        verbose_name_plural = 'Genre Categories'

    def __str__(self):
        return self.name


class ImdbMovie(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(ImdbDirector)
    number_99popularity = models.DecimalField(db_column='99popularity', max_digits=6, decimal_places=2)  # Field renamed because it wasn't a valid Python identifier.
    imdb_score = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.ManyToManyField(ImdbGenreCategory, related_name='genre')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'imdb_movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name
