from django import forms
from django.db.models import fields
from .models import Customers

class CustomerForm(forms.ModelForm):

  class Meta:
    model = Customers
    fields = "__all__"