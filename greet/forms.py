from .models import Person
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender', 'email', 'pincode', 'phone']
        labels = {
            'first_name': _("First Name"), 
            'last_name': _("Last Name"), 
            'gender': _("Gender"), 
            'email': _("Email"), 
            'pincode': _("Pincode"), 
            'phone': _("Phone Number")
        }
        help_texts = {
            'first_name': _('Some useful help text.'),
        }
    