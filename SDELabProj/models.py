from django.db import models

# Create your models here.
class attendance(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.BigIntegerField()
    att1=models.IntegerField()
    att2=models.IntegerField()
    att3=models.IntegerField()
    att4=models.IntegerField()
    att5=models.IntegerField()
    att6=models.IntegerField()

class marks(models.Model):
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()
    mark4=models.IntegerField()
    mark5=models.IntegerField()
    mark6=models.IntegerField()
