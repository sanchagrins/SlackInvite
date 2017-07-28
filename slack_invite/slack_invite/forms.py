from django import forms

class InviteForm(forms.Form):
    email_addr = forms.EmailField(label='Email addy')
