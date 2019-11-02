from django import forms
from django.forms import ModelForm
from accounts.models import customuser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class usercreationform(ModelForm):
    class Meta:
        model=customuser
        fields=('email',)
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password confirmation",widget=forms.PasswordInput)
    def clean_password(self):
        password1=forms.cleaned_data.get("password1")
        password2=forms.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")


    def save(self, commit=True):
        user=super(usercreationform, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

class userchangeform(ModelForm):
    password=ReadOnlyPasswordHashField
    class Meta:
        model=customuser
        fields=('email','password','admin','staff','active')
    def clean_password(self):
        return self.initial["password"]


class RegisterForm(ModelForm):
    class Meta:
        model=customuser
        fields=('email',)
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password confirmation",widget=forms.PasswordInput)
    def clean_password(self):
        password1=forms.cleaned_data.get("password1")
        password2=forms.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")


    def save(self, commit=True):
        user=super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user
