from django import forms

class InviteForm(forms.Form):
    email_addr = forms.EmailField(widget=forms.EmailInput({'placeholder':'Email address'}), label='')
