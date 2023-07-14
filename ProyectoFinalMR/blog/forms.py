from django import forms
from blog.models import *

class FormNewReview(forms.ModelForm):
    class Meta:
        model = review
        fields = ('titulo', 'album', 'review','albumCover')

        widgets = {
            #'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'album' : forms.TextInput(attrs={'class': 'form-control'}),
            'review' : forms.Textarea(attrs={'class': 'form-control'}),
        }