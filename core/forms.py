from django import forms
from .models import Dashboard, SbdSellOrder
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ('phone_number','bank_region', 'bank_account_number', 'bank')


class SbdSellOrderForm(forms.ModelForm):
    class Meta:
        model = SbdSellOrder
        fields = ('sbd', 'sbd_ngn', 'sbd_usd')
