from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForms(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full p-3 bg-black text-white border border-white/20 rounded-xl focus:outline-none focus:ring-2 focus:ring-white/40 shadow-white/10',
                'placeholder': 'What’s on your mind?',
                'rows': 4
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'w-full text-white bg-black border border-white/20 p-2 rounded-xl focus:outline-none'
            }),
        }
class UserRegisteration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')