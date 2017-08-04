from django import forms

class InviteForm(forms.Form):
    email_addr = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-signin input','placeholder':'Email address'}), label='')
