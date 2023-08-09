from django import forms
from .models import SwiftUser

class SignUpForm(forms.ModelForm):

    class Meta:
        model = SwiftUser
        fields = [
            'username',
            'email',
            'phone',
            'age',
            'gender',
            'role',
            'collegeName',
            'collegeID',
            'password',  # Include password field
            'profile_pic',
            'license_pic',
            'location'
        ]


                  
from django.contrib.auth.forms import AuthenticationForm  
                                                                                  
class LogInForm(AuthenticationForm):
    # Inherits from AuthenticationForm to handle login securely

    class Meta:
        model = SwiftUser               
        fields = ['email']  # Include email for authentication
                                              
class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = SwiftUser
        fields = ['profile_pic']
                         