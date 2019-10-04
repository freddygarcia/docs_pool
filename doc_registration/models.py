from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "área"
        verbose_name_plural = "  Áreas"

class Source(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "origen"
        verbose_name_plural = " Origenes"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')


    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = " Categorías"

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=300, verbose_name='Título')
    description = models.CharField(max_length=300, verbose_name='Descripción')
    source = models.ForeignKey('Source', on_delete=models.PROTECT, verbose_name='Origen')

    @property
    def update_date(self):
        return self.documentdetails_set.latest('last_update').last_update

    class Meta:
        verbose_name  = "documento"
        verbose_name_plural = " Documentos"

    def __str__(self):
        return self.title

class DocumentDetails(models.Model):
    link = models.CharField(max_length=200)
    document = models.ForeignKey('Document', on_delete=models.PROTECT)
    file_name = models.CharField(max_length=300, verbose_name='Nombre')
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.document)

    class Meta:
        verbose_name = "Detalle del documento"
        verbose_name_plural = " Detalle de los Documentos"

class Mandate(models.Model):
    content = models.TextField(verbose_name='Contenido')
    document = models.ForeignKey('Document', on_delete=models.PROTECT, verbose_name='Documento')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Categoría')
    areas = models.ManyToManyField(Area)

    @property
    def display_content(self):
        areas_len = len(self.areas.all())
        option = {6: 1100, 1 : 200, 2: 200, 3: 300, 4: 600, 5: 900 }
        text_limit = option[areas_len]
        return self.content[:text_limit] + '...'

    @property
    def areas_list(self):
        return self.areas.all()

    @staticmethod
    def find(filters):

        query = Mandate.objects.filter()

        if filters.get('category'):
            query = query.filter(category_id=filters.get('category'))

        if filters.get('area'):
            query = query.filter(areas__id=filters.get('area'))

        if filters.get('source'):
            query = query.filter(document__source_id=filters.get('source'))

        return query

    def __str__(self):
        LEN = 200
        if len(self.content) > LEN:
            return self.content[:LEN] + '...'
        return self.content

    class Meta:
        verbose_name = "mandato"
        verbose_name_plural = "Mandatos"
        