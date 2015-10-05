from django import forms

from core.models import Registration


class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    can_model = forms.BooleanField(required=False)

    def save(self, *args, **kwargs):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        can_model = self.cleaned_data['can_model']

        application = Registration(first_name=first_name, last_name=last_name,
                                   email=email, phone=phone, can_model=can_model)
        application.save()
