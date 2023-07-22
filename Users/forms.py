from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

# Form used to create a new user 
class user_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    username        = forms.CharField(min_length=5, max_length=64, required=True, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Username"}))
    first_name      = forms.CharField(min_length=1, max_length=64, required=False, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter First Name"}))
    last_name       = forms.CharField(min_length=1, max_length=64, required=False, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Last Name"}))
    email           = forms.EmailField(min_length=8, max_length=128, required=True, widget=forms.EmailInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Email"}))
    password1       = forms.CharField(min_length=8, max_length=256, required=True, widget=forms.PasswordInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Password"}))
    password2       = forms.CharField(min_length=8, max_length=256, required=True, widget=forms.PasswordInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Confirm Password"}))


# Form used to allow a user to change their password
class user_change_password(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]

    old_password    = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Password"}))
    new_password1   = forms.CharField(min_length=8, max_length=256, required=True, widget=forms.PasswordInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Password"}))
    new_password2   = forms.CharField(min_length=8, max_length=256, required=True, widget=forms.PasswordInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Password"}))


# Form used to allow a user to change their account details
class user_change_details(UserChangeForm):
    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email"]

    username        = forms.CharField(min_length=5, max_length=64, required=True, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Username"}))
    first_name      = forms.CharField(min_length=1, max_length=64, required=False, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter First Name"}))
    last_name       = forms.CharField(min_length=1, max_length=64, required=False, widget=forms.TextInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Last Name"}))
    email           = forms.EmailField(min_length=8, max_length=128, required=True, widget=forms.EmailInput(attrs={"class":"form-control mx-auto w-50 my-3", "placeholder":"Enter Email"}))
