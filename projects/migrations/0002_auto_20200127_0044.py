# Generated by Django 3.0.2 on 2020-01-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_finish',
            field=models.DateField(verbose_name='Data Final'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(verbose_name='Project ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=50, verbose_name='Nome do Projeto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start',
            field=models.DateField(verbose_name='Data Inicial'),
        ),
    ]