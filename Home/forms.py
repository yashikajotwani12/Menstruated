from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.CharField(max_length=150)
    message = forms.CharField(widget= forms.Textarea, max_length=2000)

    