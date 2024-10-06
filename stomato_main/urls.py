from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('clients/client-add/', views.ClientAdd.as_view(), name='client_add'),
    path('clients/<slug:client_slug>/', views.Client.as_view(), name='client'),
    path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    path('doctors/doctor-add/', views.DoctorAdd.as_view(), name='doctor_add'),
    path('doctors/<slug:doctor_slug>/', views.Doctor.as_view(), name='doctor'),
    path('visits/', views.VisitList.as_view(), name='visit_list'),
    path('visits/visit-add/', views.VisitAdd.as_view(), name='visit_add'),
    path('edit-visit/<int:visit_id>/', views.Visit.as_view(), name='visit'),


]