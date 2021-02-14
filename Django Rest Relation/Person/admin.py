from django.contrib import admin
from .models import Person,Thoughts


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','phone','email']

@admin.register(Thoughts)
class ThoughtsAdmin(admin.ModelAdmin):
    list_display = ['username','title','thoughts']
# Register your models here.
