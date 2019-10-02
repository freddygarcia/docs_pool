from django.db import models

# Create your models here.

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

    class Meta:
        verbose_name = "Detalle del documento"
        verbose_name_plural = " Detalle de los Documentos"

class Mandate(models.Model):
    content = models.TextField(verbose_name='Contenido')
    document = models.ForeignKey('Document', on_delete=models.PROTECT, verbose_name='Documento')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Categoría')
    area = models.ForeignKey('Area', on_delete=models.PROTECT, verbose_name='Área')

    def __str__(self):
        LEN = 200
        if len(self.content) > LEN:
            return self.content[:LEN] + '...'
        return self.content

    class Meta:
        verbose_name = "mandato"
        verbose_name_plural = "Mandatos"
