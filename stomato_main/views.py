from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from . import forms
from stomato_main.models import ClientsModel, DoctorsModel, VisitsModel
from stomato_main.utils import RequiredMixin


class HomePage(RequiredMixin, TemplateView):
    title = 'Главная страница'
    template_name = 'stomato_main/homepage.html'


class ClientList(RequiredMixin, ListView):
    model = ClientsModel
    template_name = 'stomato_main/client-list-view.html'
    title = 'Список клиентов'


class DoctorList(RequiredMixin, ListView):
    model = DoctorsModel
    template_name = 'stomato_main/doctor-list-view.html'
    title = 'Список врачей'


class VisitList(RequiredMixin, ListView):
    model = VisitsModel
    template_name = 'stomato_main/visit-list-view.html'
    title = 'Список записей'


class Client(RequiredMixin, UpdateView):
    model = ClientsModel
    template_name = 'stomato_main/client-view.html'
    slug_url_kwarg = 'client_slug'
    slug_field = 'slug'
    fields = ['fullname', 'city', 'address', 'phone', 'email',
                  'date_of_birth', 'passport_number', 'additional_info']

    '''def get_queryset(self):
        return  VisitsModel.objects.filter(client__slug=self.kwargs['client_slug'])'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = ClientsModel.objects.get(slug=self.kwargs['client_slug']).fullname
        context['title'] = f'Клиент {name}'
        context['object_list'] = VisitsModel.objects.filter(client__slug=self.kwargs['client_slug'])
        return context


class ClientAdd(RequiredMixin, CreateView):
    form_class = forms.ClientAddForm
    title = 'Новый клиент'
    template_name = 'stomato_main/client-add.html'


class Doctor(RequiredMixin, UpdateView):
    model = DoctorsModel
    template_name = 'stomato_main/doctor-view.html'
    slug_url_kwarg = 'doctor_slug'
    slug_field = 'slug'
    fields = ['photo', 'fullname', 'position', 'phone', 'email', 'job_status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = DoctorsModel.objects.get(slug=self.kwargs['doctor_slug'])
        context['object_list'] = VisitsModel.objects.filter(doctor__slug=self.kwargs['doctor_slug'])
        context['title'] = f'Врач {name}'
        return context


class DoctorAdd(RequiredMixin, CreateView):
    form_class = forms.DoctorAddForm
    title = 'Новый врач'
    template_name = 'stomato_main/doctor-add.html'


class Visit(RequiredMixin, UpdateView):
    model = VisitsModel
    template_name = 'stomato_main/visit-view.html'
    pk_url_kwarg = 'visit_id'
    fields = ['client', 'doctor', 'description',
              'record_at_date', 'record_at_time']
    success_url = reverse_lazy('visit_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = (f'Запись клиента {self.object.client} на '
                            f'{self.object.record_at_date} {self.object.record_at_time}')
        return context


class VisitAdd(RequiredMixin, CreateView):
    form_class = forms.VisitAddForm
    title = 'Новая запись'
    template_name = 'stomato_main/visit-add.html'
