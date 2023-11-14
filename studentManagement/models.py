from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    name = models.CharField(max_length=50, blank=False)
    matricula = models.CharField(max_length=50, blank=False, default="0")
    genero = models.CharField(max_length=10, blank=False, default="neutre")
    idade = models.CharField(max_length=3, blank=False, default="0")
    turma = models.CharField(max_length=50, blank=False, default="0")
    email = models.CharField(max_length=70, blank=False, default="gmail")

