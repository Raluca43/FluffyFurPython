from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from pets.models import Pets


class Adoptionrequestperpet(models.Model):
    name_of_the_apllicant = models.CharField(max_length=20)
    email_of_the_apllicant = models.EmailField(max_length=200)
    phone_number_of_the_apllicant = models.CharField(max_length=25)
    description_of_the_apllicant = models.TextField(max_length=400)
    date_time_of_the_apllicant = models.DateTimeField(default=timezone.now)
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name_of_the_apllicant} {self.city_of_the_apllicant}'


@receiver(post_save, sender=Adoptionrequestperpet)
def send_mail_to_subs(sender, instance, created, **kwargs):
    if created:
        message = '''Adoption request from Ghemotoc cu blana         '''
        send_mail(subject='adoption requested', message=message, from_email='noreply.petadoption@gmail.com',
        recipient_list=[instance.pet.email])


class Adoptionrequest(models.Model):

    name_of_the_apllicant = models.CharField(max_length=20)
    email_of_the_apllicant = models.EmailField(max_length=200)
    phone_number_of_the_apllicant = models.CharField(max_length=25)
    district_of_the_apllicant = models.CharField(null=True, blank=True, max_length=20)
    city_of_the_apllicant = models.CharField(max_length=20)
    description_of_the_apllicant = models.TextField(max_length=400)
    active_of_the_apllicant = models.BooleanField(default=True)
    date_time_of_the_apllicant = models.DateTimeField(default=timezone.now)
    pet_type = models.CharField(max_length=20)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name_of_the_apllicant} {self.city_of_the_apllicant}'