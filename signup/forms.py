from django import forms

from .models import EmailSignup

class EmailSignupForm(forms.ModelForm):

    class Meta:
        model = EmailSignup
        widgets = {
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name', 'size': '15'}),
            'last_name'  : forms.TextInput(attrs = {'placeholder': 'Last Name', 'size': '15'}),
            'email'  	 : forms.TextInput(attrs = {'placeholder': 'Email', 'size': '20'}),
        }
        fields = ('first_name', 'last_name','email')