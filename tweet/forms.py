from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet


class TweetForm(forms.ModelForm):
    """Form for creating new tweets"""
    
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'What\'s happening?',
                'maxlength': 280,
                'id': 'tweet_content'
            })
        }
        labels = {
            'content': 'Tweet Content'
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or not content.strip():
            raise forms.ValidationError('Tweet content cannot be empty!')
        
        if len(content) > 280:
            raise forms.ValidationError('Tweet cannot exceed 280 characters!')
        
        return content.strip()


class TweetEditForm(forms.ModelForm):
    """Form for editing existing tweets"""
    
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Edit your tweet...',
                'maxlength': 280
            })
        }
        labels = {
            'content': 'Tweet Content'
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or not content.strip():
            raise forms.ValidationError('Tweet content cannot be empty!')
        
        if len(content) > 280:
            raise forms.ValidationError('Tweet cannot exceed 280 characters!')
        
        return content.strip()


class UserRegistrationForm(UserCreationForm):
    """Form for user registration"""
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    """Custom login form"""
    
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    ) 