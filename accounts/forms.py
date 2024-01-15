from django.forms import ModelForm
from django import forms
from .models import User
import re

email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
number_patern = re.compile(r'^\+994 [55|50|70|77|51|10|99] [0-9]{3} [0-9]{2} [0-9]{2}$')


class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "email-input",
        "placeholder": "Confirm Password"
    }))

    class Meta:

        model = User

        fields = ("full_name", 
                  "emailornumber",
                  "password",)
        
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "email-input",
                "placeholder": "adınızı daxil edin"
            }),

            "emailornumber": forms.TextInput(attrs={
                "class": "email-input",
                "placeholder": "Email or Nömrə",
                "id":"emailornumber",
                "oninput": "validateEmailorNumber()",
            }),

            "password": forms.PasswordInput(attrs={
                "class": "email-input",
                "placeholder": "****"
            }),

        }

    def clean(self):
        super().clean()
        if self.cleaned_data['full_name']:
            name = self.cleaned_data['full_name']
            arr = name.split(" ")
            for i in arr:
                if not i.isalpha():
                    self.errors['full_name'] = self.error_class([('Wrong full name')])
        else:
            self.errors['full_name'] = self.error_class([('Empty full name')])
            self.errors['last_name'] = self.error_class([('Empty last name')])
        if self.cleaned_data['emailornumber']:
            emailornumber = self.cleaned_data['emailornumber']
            if User.objects.filter(emailornumber=self.cleaned_data['emailornumber']):
                self._errors['emailornumber']  = self.error_class([('This email or number already exists')])
            # else:
            #     if "@" in emailornumber:
            #         print(email_pattern.match(emailornumber))
            #         if email_pattern.match(emailornumber) == None:
            #             print("salam")
            #             self._errors['emailornumber']  = self.error_class([('Wrong email!')])
            #     else:
            #         if number_patern.match(emailornumber) == None:
            #             self._errors['emailornumber']  = self.error_class([('Wrong number!')])
                        
            elif emailornumber.isdigit() == False and not email_pattern.match(emailornumber):
                self._errors['emailornumber']  = self.error_class([('Wrong email or number!')])
            # elif emailornumber[-10:] != '@gmail.com':
            #     self._errors['emailornumber']  = self.error_class([('Wrong email or number!')])
        else:
            self.errors['emailornumber'] = self.error_class([('Empty email or number!')])
        if self.cleaned_data['password']:
            if len(self.cleaned_data['password']) < 8:
                self._errors['password'] = self.error_class([('Should Contain a minimum of 8 characters')])
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                self._errors['confirm_password']  = self.error_class([('Not same password!')])
        else:
            self.errors['password'] = self.error_class([('Empty Password!')])