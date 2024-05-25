from django.db import models


# Create your models here.
class Booking(models.Model):
   id=models.IntegerField(primary_key=True)
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model): 
    Id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    inventory = models.IntegerField()

    def __str__(self):
        return self.name