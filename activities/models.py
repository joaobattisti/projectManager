from django.db import models
from projects.models import Project

class Activity(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='ID do Projeto')
    activity_name = models.CharField(max_length=50, verbose_name='Nome da Atividade')
    activity_datestart = models.DateField(verbose_name='Data Inicial')
    activity_datefinish = models.DateField(verbose_name='Data Final')
    activity_concluded = models.BooleanField(default=False, verbose_name='Atividade Concluida')


