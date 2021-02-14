from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    email = models.EmailField(verbose_name='Email',max_length=50,unique=True)
    phone = models.BigIntegerField(verbose_name='Phone Number',unique=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth')

    def __str__(self):
        return self.first_name + ' ' + self.last_name