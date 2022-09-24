from django import forms 
from .models import SpaceX

class Data(forms.ModelForm):
    class Meta:
        model=SpaceX
        fields=['Name','Password','Field']
