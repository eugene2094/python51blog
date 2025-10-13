from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'published_date', 'auther')


# class RegisterForm(UserCreationForm):
#     phone = forms.CharField(max_length=20, required=False)
#     city = forms.CharField(max_length=100, required=False)
#     birth_date = forms.DateTimeField(null=True, required=False)
#     avatar = forms.URLField(null=True, required=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'city', 'birth_date', 'avatar')
