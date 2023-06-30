from django.db import models
from worker.models import Worker


class Vacancy(models.Model):
    title = models.CharField(max_length=255,verbose_name='Вакансия')
    salary = models.IntegerField(null=True, blank=True,verbose_name='Зарплата')
    description = models.TextField(default='Нет описания',verbose_name='Описание')
    is_relevant = models.BooleanField(default=True, verbose_name='Актуальность')
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    category = models.ForeignKey(
        to='Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name_company = models.CharField(max_length=255,verbose_name='Название компании')
    address_company = models.CharField(max_length=255,verbose_name='Адрес компании')
    number_of_employees= models.IntegerField(null=True,blank=True, verbose_name='Число сотрудников')
    is_hanting=models.BooleanField(default=True,verbose_name='Ищет сотрудников')
    def __str__(self):
        return self.name_company