from django.contrib import admin
from .models import SpaceX

# Register your models here.
@admin.register(SpaceX)
class listAdmin(admin.ModelAdmin):
    list_display=('id','Name','Password','Field')