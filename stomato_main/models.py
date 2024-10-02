from datetime import datetime
from django.db import models


class JobStatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(job_status='Уволен')


class Clients(models.Model):
    fullname = models.CharField(max_length=100)
    additional_info = models.TextField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['fullname', 'passport_number']


class Doctors(models.Model):
    photo = models.ImageField(upload_to='photos/')
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    job_status = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name_plural = 'Врачи'
        verbose_name = 'Врач'
        ordering = ['fullname']


class Visits(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.PROTECT)
    description = models.TextField()
    record_at_date = models.DateField()
    record_at_time = models.TimeField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['client', 'record_at_date', 'record_at_time']