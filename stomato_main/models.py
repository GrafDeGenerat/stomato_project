from django.db import models
from django.urls.base import reverse
from django_extensions.db.fields import AutoSlugField
from transliterate import slugify as transliterate_slugify
import datetime


class JobStatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(job_status=DoctorsModel.Status.DISMISSED)


class UpToDateVisitsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(record_at_date__gte=datetime.date.today(),
                                             record_at_time__gte=datetime.datetime.now())


class ClientsModel(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    additional_info = models.TextField(verbose_name='Дополнительно', null=True)
    address = models.CharField(max_length=100, verbose_name='Адрес', null=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True)
    passport_number = models.CharField(max_length=100, unique=True, verbose_name='Паспорт')
    email = models.CharField(max_length=100, verbose_name='Эл. почта', null=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    slug = AutoSlugField(max_length=100, unique=True, db_index=True, verbose_name='url',
                         populate_from='fullname', slugify_function=transliterate_slugify, overwrite=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['fullname', 'passport_number']

    def __str__(self):
        return f'{self.fullname}'

    def get_absolute_url(self):
        return reverse('client', kwargs={'client_slug': self.slug})


class DoctorsModel(models.Model):
    class Status(models.IntegerChoices):
        DISMISSED = 0, 'Уволен'
        WORKED = 1, 'Работает'
        VACATION = 2, 'Отпуск'
        SICK = 3, 'Больничный'

    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Фото')
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.ManyToManyField('PositionModel', blank=True, related_name='positions_of_doctor')
    email = models.CharField(max_length=100, verbose_name='Эл. почта', null=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    job_status = models.IntegerField(choices=Status.choices,
                                     default=Status.WORKED, verbose_name='Статус работы')
    slug = AutoSlugField(max_length=100, unique=True, db_index=True, verbose_name='url',
                         populate_from='fullname', slugify_function=transliterate_slugify, overwrite=True)
    status = JobStatusManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Врачи'
        verbose_name = 'Врач'
        ordering = ['fullname']

    def __str__(self):
        return f'{self.fullname}'

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'doctor_slug': self.slug})


class VisitsModel(models.Model):
    client = models.ForeignKey(ClientsModel, on_delete=models.CASCADE, verbose_name='ФИО клиента')
    doctor = models.ForeignKey(DoctorsModel, on_delete=models.PROTECT, verbose_name='ФИО врача')
    description = models.TextField(verbose_name='Описание')
    record_at_date = models.DateField(verbose_name='Дата')
    record_at_time = models.TimeField(verbose_name='Время')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    objects = models.Manager()
    up_to_date = UpToDateVisitsManager()

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['record_at_date', 'record_at_time', 'client', ]

    def __str__(self):
        time = self.record_at_time.strftime("%H:%M")
        date = self.record_at_date.strftime("%d.%m.%Y")
        return f'{self.client.fullname} на {date} {time}'

    def get_absolute_url(self):
        return reverse('visit', kwargs={'visit_id': self.pk})


class PositionModel(models.Model):
    position = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Должность')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')

    def __str__(self):
        return self.position
