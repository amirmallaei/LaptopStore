from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from user.models import Profile


User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICE)
    address = forms.CharField(widget=forms.Textarea, required=False) 

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'gender','first_name', 'last_name',
                 'password', 'password2','address']

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')

        if pass1!=pass2:
            raise ValidationError("Password Do Not Match!")
        return pass2
    
    def clean_gender(self):
        gen = self.cleaned_data.get('gender')
        if gen in ["", None, "0"]: 
            raise ValidationError("Gender must be selected!")
        return gen


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

