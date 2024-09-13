
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture')

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = forms.ValidationError(
                'The first name cannot be the same as the last name', code='invalid')

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', forms.ValidationError(
                    'E-mail já cadastrado', code='invalid')
            )

        return email
