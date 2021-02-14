from django.db import models

# Create your models here.
class Person(models.Model):
    username   = models.SlugField(verbose_name = 'username',max_length=10,blank= False,null=False)
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    email = models.EmailField(verbose_name='Email',max_length=50,unique=True)
    phone = models.BigIntegerField(verbose_name='Phone Number',unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Thoughts(models.Model):
    username = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='thoughts')
    title  = models.CharField(max_length=50)
    thoughts = models.TextField(verbose_name='Thoughts')

    def __str__(self):
        return self.title
