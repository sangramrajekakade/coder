from django import forms
from django.forms import ModelForm, formset_factory, ModelChoiceField
from .models import *


class ContactForm(ModelForm):

  class Meta:
    model = Contact
    fields = '__all__'
    # exclude = ['user','Is_salesBranches']
