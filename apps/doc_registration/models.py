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
    description = models.CharField(
        max_length=300, verbose_name='Descripción', null=True, blank=True)
    source = models.ForeignKey(
        'Source', on_delete=models.PROTECT, verbose_name='Origen')

    @property
    def recent_details(self):
        return self.document_details.latest('last_update')

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = " Documentos"

    def __str__(self):
        return self.title


class DocumentDetails(models.Model):
    link = models.CharField(max_length=200)
    document = models.ForeignKey(
        'Document', on_delete=models.PROTECT, related_name="document_details")
    file_name = models.CharField(max_length=300, verbose_name='Nombre')
    last_update = models.DateTimeField(auto_now=True)
    document_date = models.DateField(null=True, verbose_name='Fecha Documento')

    def __str__(self):
        return self.document.title

    class Meta:
        verbose_name = "Detalle del documento"
        verbose_name_plural = " Detalle de los Documentos"


class Mandate(models.Model):
    content = models.TextField(verbose_name='Contenido')
    document_ref = models.ForeignKey(
        'DocumentDetails', on_delete=models.PROTECT, verbose_name='Documento',
        related_name='mandates')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name='Categoría')
    areas = models.ManyToManyField(Area)

    MANDATE_TYPE_CHOICES = [
        ('MUST', 'Debe'),
        ('MUST_NOT', 'No debe'),
    ]

    type = models.CharField(
        max_length=10,
        db_column='m_type',
        choices=MANDATE_TYPE_CHOICES,
        verbose_name='Tipo',
        default='MUST',
    )

    @property
    def display_content(self):
        areas_len = len(self.areas.all())
        option = {0: 100, 1: 200, 2: 400, 3: 500, 4: 600, 5: 900, 6: 1100}
        text_limit = option[areas_len]

        if len(self.content) > text_limit:
            return self.content[:text_limit] + '...'
        return self.content

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

        if filters.get('document'):
            query = query.filter(document__id=filters.get('document'))

        if filters.get('source'):
            query = query.filter(document__source_id=filters.get('source'))

        if filters.get('keyword'):
            query = query.filter(content__icontains=filters.get('keyword'))

        return query

    def __str__(self):
        LEN = 50
        if len(self.content) > LEN:
            return self.content[:LEN] + '...'
        return self.content

    class Meta:
        verbose_name = "mandato"
        verbose_name_plural = "Mandatos"


class MandateTest(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    mandate = models.ForeignKey(
        'Mandate', on_delete=models.PROTECT, related_name='tests')

    def __str__(self):
        return f'{self.mandate}: {self.name}'

    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"
