from django.db import models

# Create your models here.


from datetime import timedelta
from urllib.parse import urlparse
from django.utils.text import slugify

from django.db import models
from django.template.defaultfilters import pluralize
from django.utils import timezone
from django.urls import reverse
from app.managers import CustomDbManager


class PostGresDBManager(models.Model):

    use_db = 'postgres'
    objects = CustomDbManager()

    class Meta:
        abstract = True


class Source(PostGresDBManager):
    class Meta:
        db_table = 'news_sources'
        verbose_name = 'fuente'
        verbose_name_plural = 'fuentes'

    name = models.CharField(max_length=255)
    always = models.BooleanField(default=False)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

class KeyWord(PostGresDBManager):
    class Meta:
        db_table = 'keywords'
        verbose_name = 'palabra clave'
        verbose_name_plural = 'palabras claves'

    name = models.CharField(max_length=255)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

class SourceLink(PostGresDBManager):
    class Meta:
        db_table = 'source_links'
        verbose_name = 'enlace a fuente'
        verbose_name_plural = 'enlaces a fuentes'

    source = models.ForeignKey(Source,
        on_delete=models.PROTECT,
        blank = True,
        null=True
        )
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return ("{} - {}").format(self.source.name, self.name)

class Post(PostGresDBManager):
    class Meta:
        db_table = 'news_posts'
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'

    source_link = models.ForeignKey(SourceLink,
        on_delete=models.PROTECT,
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    body = models.TextField()
    image = models.CharField(max_length=500)
    url = models.URLField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {}".format(self.source_link.source.name,
            self.title)
