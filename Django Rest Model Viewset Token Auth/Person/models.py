from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    email = models.EmailField(verbose_name='Email',max_length=50,unique=True)
    phone = models.BigIntegerField(verbose_name='Phone Number',unique=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)