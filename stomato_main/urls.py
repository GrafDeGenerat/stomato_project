from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    path('visits/', views.VisitList.as_view(), name='visit_list'),

]