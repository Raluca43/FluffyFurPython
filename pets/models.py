from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Pets(models.Model):

    GENDER_OPTION = (('male', 'Male'), ('female', 'Female'))
    ANIMAL_CAT_OR_DOG = (('dog', 'dog'), ('cat', 'cat'), ('other', 'other pets'))
    ANIMAL_TYPE_OPTION = (('puppy', 'puppy'), ('kitten', 'kitten'), ('small size', 'small size'), ('medium size', 'medium size'),
                          ('high size', 'high size'), ('vaccine', 'vaccine'), ('sterilized', 'sterilized'))

    announce_title = models.CharField(max_length=20)
    animal_type = models.CharField(choices=ANIMAL_CAT_OR_DOG, max_length=10)
    animal_description = models.CharField(max_length=1000)
    animal_label = models.CharField(choices=ANIMAL_TYPE_OPTION, max_length=11)
    another_label_description = models.CharField(null=True, blank=True, max_length=255)
    district = models.CharField(null=True, blank=True, max_length=20)
    city = models.CharField(max_length=20)
    pet_image = models.ImageField(null=True, blank=True, upload_to='static/images/')
    animal_name = models.CharField(null=True, blank=True, max_length=12)
    animal_age = models.CharField(max_length=7)
    gender = models.CharField(choices=GENDER_OPTION, max_length=6)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    date_time = models.DateField(default=timezone.now)
    active = models.BooleanField(null=True, blank=True, default=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.animal_name} {self.animal_label}'
