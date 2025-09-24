from django.db import models

class Autor(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=20)
    surnabe = models.CharField('Фамилия', max_length=25)
    birthday = models.DateField('Дата рождения')
    bio = models.TextField('Биография')

class PUblisher(models.Model):
    name = models.CharField('НАзвание', unique=True)

class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    id_publisher = models.ForeignKey(PUblisher, on_delete=models.CASCADE)
    id_autor = models.ManyToManyField(Autor)
