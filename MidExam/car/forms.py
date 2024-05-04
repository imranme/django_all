from django import forms 
from . models import CarModel,CommentsModel


class CarForm(forms.ModelForm):
    
    class Meta:
        model=CarModel
        exclude=['slug','customer']
        labels={
            'BrandName':'Brand Name',
            'ReleaseDate':'Release Date',
            'Name':'Car Name',
        }
        widgets={
            'ReleaseDate':forms.DateInput(attrs={'type':'date'}),   
        }
   

class CommentForm(forms.ModelForm):

    class Meta:
        model=CommentsModel
        exclude=['car']






