from django import forms
from .models import SwiftUser,ROLE_CHOICES

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
            'password',
            'profile_pic',
            'license_pic',
        ]



class LogInForm(forms.ModelForm):
    class Meta:
        model = SwiftUser
        fields = [
            'email',       
            'password',            
        ]



class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = SwiftUser
        fields = ['profile_pic']
