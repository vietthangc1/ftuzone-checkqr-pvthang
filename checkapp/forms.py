from django import forms
from django.db.models import fields
from .models import Customers, UserProfile
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):

  class Meta():
    model = Customers
    fields = "__all__"

  def __init__(self, *args, **kwargs):
    super(CustomerForm, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs['class'] = 'form-control'
    self.fields['CardId'].widget.attrs['class'] = 'form-control'
    self.fields['YearofBirth'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['phone'].widget.attrs['class'] = 'form-control'
    self.fields['school'].widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):
  class Meta():
    fields = ('username', 'password')