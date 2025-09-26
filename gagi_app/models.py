from django.db import models

class Users(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=25)
    birthday = models.DateField('Дата рождения')
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('e-mail', max_length=100)
    hash_password = models.CharField('Пароль', max_length=255)
    created_at = models.DateTimeField('Дата и время регистрации')
    def __str__(self):
        return f"{self.surname}{self.name}"

    class Meta: 
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]
        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "email"],
                name = "unique_surname_email"
            ),
            
        ]


# class PUblisher(models.Model):
#     name = models.CharField('НАзвание', unique=True)

# class Book(models.Model):
#     title = models.CharField('Название', max_length=50)
#     id_publisher = models.ForeignKey(PUblisher, on_delete=models.CASCADE)
#     id_autor = models.ManyToManyField(Author)

