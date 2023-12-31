from django import forms
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormNewReview(forms.ModelForm):
    class Meta:
        model = review
        fields = ('author','titulo', 'album', 'review','score','albumCover')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author_id', 'type':'hidden',}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'album' : forms.TextInput(attrs={'class': 'form-control'}),
            'review' : forms.Textarea(attrs={'class': 'form-control'}),
            'score' : forms.Select(attrs={'class': 'form-control'}),
        }
                                         
class UserEditForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    description= forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Descripcion"}))
    link= forms.URLField(widget= forms.TextInput(attrs={"placeholder":"Links"}))
    


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Old password"}))
    new_password1 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"New password"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author_id', 'type':'hidden',})}
        

class AvatarForm(forms.Form):
    avatar = forms.ImageField()