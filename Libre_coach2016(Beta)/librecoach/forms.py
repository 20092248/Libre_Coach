from django.contrib.admin import widgets
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail

from SiteWeb import settings


class CreateAccountform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','date_joined']
        #fields = '__all__'

class CreateAccountformAdm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password','is_staff','is_active','is_superuser','date_joined']
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
                raise ValueError("L'utilisateur n'existe pas.")
            if not user.check_password(password):
                raise ValueError("Mot de passe incorrect!")
        return super(Loginform, self).clean(*args, **kwargs)

class ContactForm(forms.Form):

    full_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary

        form_full_name = self.cleaned_data.get('full_name')
        form_message = self.cleaned_data.get('message')
        form_email = self.cleaned_data.get('email')



        pass