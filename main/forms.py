from django import forms


class ContactForm(forms.Form):
    telephone = forms.CharField(max_length=100)
    full_name = forms.CharField(max_length=100)
