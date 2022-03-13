from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Repeat Password",
                                      widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_repeat_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['repeat_password']:
            raise forms.ValidationError("Password don't match")
        return cleaned_data['repeat_password']
