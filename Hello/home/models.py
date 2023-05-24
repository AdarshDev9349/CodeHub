from django.db import models

# Create your models here
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=90)
    email=models.CharField(max_length=80)
    issue=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Mail from ' +  self.name

class join(models.Model):
    names= models.CharField(max_length=200)
    emails=models.CharField(max_length=80)
    describe= models.CharField(max_length=90)
   



