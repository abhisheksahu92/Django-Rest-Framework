from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class PersonGenericAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','date_of_birth']