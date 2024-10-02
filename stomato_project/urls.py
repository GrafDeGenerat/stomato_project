from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from stomato_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stomato_main.urls')),
]
