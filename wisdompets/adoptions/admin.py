from django.contrib import admin

from .models import Pet

@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
    #displays the full names of animals in the Admmin panel, otherwise it is shown as Pet Object
    list_display = ['name', 'species','breed', 'age', 'sex']

