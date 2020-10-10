from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="nom d'utilisateur", max_length=100, required=True)
    password = forms.CharField(label="mot de passe", max_length=100, required=True, widget=forms.PasswordInput)
    
