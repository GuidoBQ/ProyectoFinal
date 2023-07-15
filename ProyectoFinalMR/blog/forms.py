from django import forms
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class FormNewReview(forms.ModelForm):
    class Meta:
        model = review
        fields = ('titulo', 'album', 'review','score','albumCover')

        widgets = {
            #'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'album' : forms.TextInput(attrs={'class': 'form-control'}),
            'review' : forms.Textarea(attrs={'class': 'form-control'}),
            'score' : forms.Select(attrs={'class': 'form-control'}),
        }