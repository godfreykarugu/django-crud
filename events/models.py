from django.db import models

# Create your models here.

class Venue(models.Model):
    name=models.CharField(max_length=200)
    addres = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,blank=True)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name
    
  
    
class Members(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Event(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateTimeField()
    Venue = models.ForeignKey(Venue,null=True,on_delete=models.CASCADE)
    manager=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    attendees = models.ManyToManyField(Members,blank=True)

    def __str__(self):
        return self.name
    


    

