from django.db import models
from catagories.models import Category
from author.models import Author

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    Category = models.ManyToManyField(Category)
    #ekta post multiple categorir moddhe thakte pare aber ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

##hello tushar your are tray too next time 