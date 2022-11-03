from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, Textarea, ClearableFileInput, EmailInput

from pets.models import Pets


class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = '__all__'
        exclude = ['poster', 'active']

        widgets = {
            'announce_title': TextInput(attrs={'placeholder': 'Please enter the announcement title',
                                               'class': 'form-control'}),
            'animal_type': Select(attrs={'class': 'form-control'}),
            'animal_description': Textarea(attrs={'placeholder': 'Please enter the dog description',
                                                  'class': 'form-control'}),
            'animal_label': Select(attrs={'class': 'form-control'}),
            'another_label_description': TextInput(attrs={'placeholder': 'Please enter a significant short '
                                                                         'descriptions', 'class': 'form-control'}),
            'district': TextInput(attrs={'placeholder': 'Please enter the district', 'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'Please enter the city', 'class': 'form-control'}),
            'pet_image': ClearableFileInput(attrs={'class': 'form-control'}),
            'animal_name': TextInput(attrs={'placeholder': 'Please enter the dog name', 'class': 'form-control'}),
            'animal_age': TextInput(attrs={'placeholder': 'Please enter the dog age', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter your user name', 'class': 'form-control'}),
            # 'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
