from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=122)
    jobtitle=models.CharField(max_length=122)
    email=models.EmailField()
    gitlink=models.CharField(max_length=122)
    linkd=models.CharField(max_length=122)
    number=models.IntegerField()
    profile=models.CharField(max_length=322)
    skill1=models.CharField(max_length=122)
    skill2=models.CharField(max_length=122)
    skill3=models.CharField(max_length=122)
    technichal1=models.CharField(max_length=122)
    technichal2=models.CharField(max_length=122)
    technichal3=models.CharField(max_length=122)
    technichal4=models.CharField(max_length=122)
    technichal5=models.CharField(max_length=122)
    companyname=models.CharField(max_length=122)
    jobtype=models.CharField(max_length=122)
    sdate=models.DateField()
    edate=models.DateField()
    uname=models.CharField(max_length=122)
    dptname=models.CharField(max_length=122)
    cgpa=models.IntegerField()
    profile_image=models.ImageField(upload_to="profiles")


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.subject



   
    

