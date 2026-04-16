from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms 

class RegisterForm(UserCreationForm):
    # Create form from User model include username, email and password, confirm password 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')
            
            if password1 and password2 and password1 != password2 :
                raise ValidationError("Password Not Matched")
            return cleaned_data
            
            
        def validate_email(self):
            email = self.cleaned_data.get('email')
            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError("Invalid email address")
            return email
        
                        
class LoginForm(forms.Form):
    # Login form field only username and password 
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())    
    
