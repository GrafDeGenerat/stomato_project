from django import forms
from . import models


class ClientAddForm(forms.ModelForm):
    class Meta:
        model = models.ClientsModel
        fields = ['fullname', 'city', 'address', 'phone', 'email',
                  'date_of_birth', 'passport_number', 'additional_info']
        widgets = {'date_of_birth': forms.DateInput(),
                   'additional_info': forms.Textarea(attrs={'rows': 5,
                                                            'cols': 40}),
                   }


class DoctorAddForm(forms.ModelForm):
    class Meta:
        model = models.DoctorsModel
        fields = ['photo', 'fullname', 'position', 'phone', 'email',
                  'job_status', ]
        widgets = {'photo': forms.ClearableFileInput(attrs={'multiple': False}),
                   'position': forms.SelectMultiple(),
                   'job_status': forms.Select,
                   }


class VisitAddForm(forms.ModelForm):
    class Meta:
        model = models.VisitsModel
        fields = ['client', 'doctor', 'description', 'record_at_date', 'record_at_time',]
        widgets = {'client': forms.Select(),
                   'doctor': forms.Select(),
                   'description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
                   'record_at_date': forms.DateInput(),
                   'record_at_time': forms.TimeInput(),
                   }

