from django import forms
from django.forms import TextInput, EmailInput, NumberInput, Textarea, DateInput

from adoptionrequest.models import Adoptionrequest, Adoptionrequestperpet


class AdoptionrequestperpetForm(forms.ModelForm):
    class Meta:
        model = Adoptionrequestperpet
        fields = ['name_of_the_apllicant', 'email_of_the_apllicant', 'phone_number_of_the_apllicant',
                  'description_of_the_apllicant', 'date_time_of_the_apllicant', 'pet' ]

        widgets = {
            'name_of_the_apllicant': TextInput(attrs={'placeholder': 'Please enter your name', 'class': 'form-control'}),
            'email_of_the_apllicant': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone_number_of_the_apllicant': NumberInput(attrs={'placeholder': 'Please enter your phone number',
                                               'class': 'form-control'}),
            'description_of_the_apllicant': Textarea(attrs={'placeholder': 'Please enter the your description',
                                                  'class': 'form-control'}),
            'date_time_of_the_apllicant': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pet': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AdoptionrequestForm(forms.ModelForm):
    class Meta:
        model = Adoptionrequest
        fields = ['name_of_the_apllicant', 'email_of_the_apllicant', 'phone_number_of_the_apllicant',
                  'city_of_the_apllicant', 'description_of_the_apllicant', 'date_time_of_the_apllicant', 'pet_type' ]

        widgets = {
            'name_of_the_apllicant': TextInput(attrs={'placeholder': 'Please enter your name', 'class': 'form-control'}),
            'email_of_the_apllicant': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone_number_of_the_apllicant': NumberInput(attrs={'placeholder': 'Please enter your phone number',
                                               'class': 'form-control'}),
            'district_of_the_apllicant': TextInput(attrs={'placeholder': 'Please enter the district', 'class': 'form-control'}),
            'city_of_the_apllicant': TextInput(attrs={'placeholder': 'Please enter the city', 'class': 'form-control'}),
            'description_of_the_apllicant': Textarea(attrs={'placeholder': 'Please enter the your description',
                                                  'class': 'form-control'}),
            'date_time_of_the_apllicant': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pet_type': TextInput(attrs={'placeholder': 'Please enter the pet type', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)