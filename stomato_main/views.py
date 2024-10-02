from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from stomato_main.utils import RequiredMixin


class HomePage(RequiredMixin, TemplateView):
    title = 'Главная страница'
    template_name = 'stomato_main/homepage.html'


class ClientList(RequiredMixin, ListView):
    pass


class DoctorList(RequiredMixin, ListView):
    pass


class VisitList(RequiredMixin, ListView):
    pass
