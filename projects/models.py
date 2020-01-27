from django.db import models

class Project(models.Model):
    project_id = models.IntegerField(verbose_name='Project ID')
    project_name = models.CharField(max_length=50, verbose_name='Nome do Projeto')
    project_start = models.DateField(verbose_name='Data Inicial')
    project_finish = models.DateField(verbose_name='Data Final')

    def __str__(self):
        return self.project_name