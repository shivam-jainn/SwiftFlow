from django import forms
from .models import CustomUser,ROLE_CHOICES

class SignUpForm(forms.ModelForm):

    class Meta:
        model = CustomUser
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
        model = CustomUser
        fields = [
            'email',       
            'password',            
        ]



class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic']
