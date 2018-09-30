from django import forms
from django.contrib.auth.models import User


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # hide user input

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        #  Saving with commit=False gets you a model object, then you can add your extra data and save it.
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # self.cleaned_data contains user data which passed validation
        user.save()

        return user
