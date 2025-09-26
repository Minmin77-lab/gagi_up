from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=20)
    surname = models.CharField('Фамилия', max_length=25)
    birthday = models.DateField('Дата рождения')
    bio = models.TextField('Биография')
    desc = models.CharField("Умер или нет", default="No")

    class Meta: 
        verbose_name = "Автор"
        verbose_name_plural = "Автор"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]
        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            
        ]

class PUblisher(models.Model):
    name = models.CharField('НАзвание', unique=True)

class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    id_publisher = models.ForeignKey(PUblisher, on_delete=models.CASCADE)
    id_autor = models.ManyToManyField(Author)

def __str__(self):
    return f"{self.surname}{self.name}"