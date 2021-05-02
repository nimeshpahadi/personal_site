from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs=
        {
        'class': 'form-control', 'placeholder': 'Write Something Here !!!', 'rows':'4', 'cols':'50'
        }
        ))
    class Meta:
        model = Comment
        fields = ('body',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)