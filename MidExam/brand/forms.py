from django import forms 
from . models import BrandModel


class BrandForm(forms.ModelForm):

    class Meta:
        model=BrandModel

        exclude ='slug'

        labels={
            'ManufactureCountry':'Manufacture Country',
        }   