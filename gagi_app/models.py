from django.db import models

class Users(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=25)
    birthday = models.DateField('Дата рождения')
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('e-mail', max_length=100, unique=True)
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

class Staff(models.Model):
    # сделать tip для должности
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    position = models.CharField('Должность', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=20)
    passport = models.CharField('Паспорт', max_length=13, unique=True)
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.position}"
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["name", "surname", "position"]
        indexes = [
            models.Index(fields=["position"])
        ]
        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "passport"],
                name = "unique_surname_passport"
            ),
        ]

class Attractions(models.Model):
    # сделать tip для роста, возраста, вместимости и продолжительности
    name = models.CharField('Название', max_length=100, unique=True)
    min_height = models.IntegerField('Минимальный рост')
    max_height = models.IntegerField('Максимальный рост')
    min_age = models.IntegerField('Минимальный возраст')
    activity_status = models.BooleanField('Статус активности', default=True)
    capacity = models.IntegerField('Вместимость')
    duration_seconds = models.IntegerField('Продолжительность (сек)')
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответственный сотрудник')
    
    def __str__(self):
        return f"{self.name} {self.staff}"
    
    class Meta:
        verbose_name = "Аттракцион"
        verbose_name_plural = "Аттракционы"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields = ["name"],
                name = "unique_name_of_attraction"
            ),
        ]

class TicketTypes(models.Model):
    # сделать tip для цены, названия, срока действия
    name = models.CharField('Название', max_length=50, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    validity_duration = models.IntegerField('Срок действия (дни)')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип билета"
        verbose_name_plural = "Типы билетов"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields = ["name"],
                name = "unique_name_of_type"
            ),
        ]




# class PUblisher(models.Model):
#     name = models.CharField('НАзвание', unique=True)

# class Book(models.Model):
#     title = models.CharField('Название', max_length=50)
#     id_publisher = models.ForeignKey(PUblisher, on_delete=models.CASCADE)
#     id_autor = models.ManyToManyField(Author)

