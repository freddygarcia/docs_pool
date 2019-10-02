# Generated by Django 2.2.5 on 2019-10-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_registration', '0002_auto_20191001_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdetails',
            name='document',
            field=models.ForeignKey(default=1, on_delete='PROTECT', to='doc_registration.Document'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='documentdetails',
            name='file_name',
            field=models.CharField(max_length=300),
        ),
    ]