from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact name'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact number'}),
        }