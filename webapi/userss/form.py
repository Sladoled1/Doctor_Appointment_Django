from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Client,User,Reservation,Worker,WorkLocation
from django import forms
from django.forms.widgets import SelectDateWidget
import datetime

class CustomerRegisterForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        client=Client.objects.create(user=user)
        client.save()
        return user


class AppointmentForm(forms.ModelForm):
    day = forms.DateField()
    start_reserv = forms.TimeField()

    class Meta:
        model=Reservation
        fields=['start_reserv','procedure']

    @transaction.atomic
    def save(self,cl,doc):
        reserv = Reservation.objects.create(client=cl,docid=doc)
        reserv.procedure = self.cleaned_data.get('procedure')
        reserv.day = self.cleaned_data.get('day')
        reserv.start_reserv = self.cleaned_data.get('start_reserv')
        if reserv.procedure==('Consultation', 'Consultation'):
            plustime = 15
        else:
            plustime = 30

        reserv.end_reserv = (datetime.datetime.combine(datetime.date(1, 1, 1), reserv.start_reserv) + datetime.timedelta(minutes=plustime)).time()
        reserv.save()
        return reserv

