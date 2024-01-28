'''
This form helps us add an email field during registration
The form provided by django '{{ form.as_p}}' does not have email

'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField() # Takes False/ True agument. Determines whether the email is optional. True by default

    #  This class gives us a nested namespace for configurations and keeps the configurations in one place
    class Meta:
        model = User # Specified the model the form will interact with
        fields= ['username', 'email', 'password1', 'password2'] # Field to be shown in our form. And the order