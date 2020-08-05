from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegistrationForm(UserCreationForm):              #this class inherits from UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.TextInput(attrs={'size':10})
    city = forms.CharField(max_length=50)
    class Meta:
        model = Profile
        fields = ['bio', 'city','image']