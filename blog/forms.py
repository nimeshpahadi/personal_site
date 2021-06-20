from .models import Comment
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs=
        {
        'class': 'form-control', 'placeholder': 'Write a comment...', 'rows':'4', 'cols':'50'
        }
        ))
    class Meta:
        model = Comment
        fields = ('body',)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
