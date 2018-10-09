from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # hide user input

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')

        if not username:
            raise forms.ValidationError('username is required!')
        if not password:
            raise forms.ValidationError('password is required!')
        if not email:
            raise forms.ValidationError('email is required!')

        # if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
        #     raise forms.ValidationError('This user already exists!')

        return super(UserSignupForm, self).clean(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    def save(self):
        #  Saving with commit=False gets you a model object, then you can add your extra data and save it.
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # self.cleaned_data contains user data which passed validation
        user.save()

        return user
