from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeCheckMixin, DateTimeField

class User(models.Model):
    
    UserName=models.CharField(max_length = 30)

    Email=models.CharField(max_length = 100)

    Password=models.CharField(max_length = 30)

    Phone=models.CharField(max_length = 20)

    def __str__(self):
        return self.UserName
  
class Book(models.Model):

    Tittle=models.CharField(max_length = 50)

    ISBN=models.CharField(max_length = 50)

    PublicationYear=models.DateField()

    Author=models.CharField(max_length = 30)

    Available=models.BooleanField(default=True) 
    def __str__(self):
        return self.Tittle

     

class BookRecord(models.Model):

    book_title = models.CharField(max_length = 100, default = 'No title')

    user_email = models.CharField(max_length = 100, default = 'No email')

    Took_On=models.DateField()

    Return_On=models.DateField()

    def __str__(self):
       return self.book_title
      
    