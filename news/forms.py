from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = "__all__"
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": 'form-control'}),
            "content": forms.Textarea(attrs={"class": 'form-control', 'rows': 5}),
            "category": forms.Select(attrs={"class": 'form-control'}),
        }
    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r'\d', title):
            raise ValidationError("Title  must not  begin with number")
        return title