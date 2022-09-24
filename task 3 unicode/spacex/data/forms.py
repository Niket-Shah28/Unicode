from django import forms 

class InfoForm(forms.Form):
    Name=forms.CharField()
    Password=forms.CharField()
    Field=forms.ChoiceField(choices=(('----','----'),('details','details'),('links','links'),('mission_name','mission_name'),('rocket','rocket')))