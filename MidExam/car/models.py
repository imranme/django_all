from django.db import models
from brand.models import BrandModel
import datetime
from django.contrib.auth.models import User
# Create your models here.

class CarModel(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Price=models.DecimalField(max_digits=10,decimal_places=5)
    Quantity=models.IntegerField()
    Description=models.TextField()
    BrandName=models.ForeignKey(to=BrandModel,on_delete=models.CASCADE)
    ReleaseDate=models.DateField()
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="customer")
    Image=models.ImageField(upload_to='car/media/images/',blank=True,null=True)
    
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.Name 
    
class CommentsModel(models.Model):
    car=models.ForeignKey(CarModel, related_name="comments",on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Body=models.TextField()
    CreatedDate=models.DateField(auto_now_add=True)
 
    def __str__(self) -> str:
        return f'Comment by {self.Name}'


