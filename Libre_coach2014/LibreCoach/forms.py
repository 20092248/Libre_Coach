from django.contrib.admin import widgets
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

class CreateAccountform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','date_joined']
        #fields = '__all__'

class Loginform(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #    user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("L'utilisateur n'existe pas")
            if not user.check_password(password):
                raise forms.ValidationError
            if not user.is_active:
                raise forms.ValidationError("L'utilisateur n'est pas encore activé.")
        return super(Loginform, self).clean(*args, **kwargs)

class Contactform(forms.Form):

    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)