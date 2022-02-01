from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Hasło'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username = username).exists():
            raise forms.ValidationError(f'Username {username} nie znaleziono w systemie')

        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError(f'Nie poprawne hasło')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(forms.ModelForm):

    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Hasło"
        self.fields['confirm_password'].label = "Podtwierdzenie hasła"

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Name {username} already exists")
        return username

    def clean (self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords are not the same')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']