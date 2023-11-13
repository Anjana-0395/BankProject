from turtle import mode

from django.db import models

# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.district_name
class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch_name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.branch_name

class NewMember(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    gender_select=(('m','Male'),('f','Female'),('o','Others'))
    gender = models.CharField(max_length=10,choices=gender_select,default=None)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.SET_NULL,blank=True,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,blank=True,null=True,default=None)
    account_select = (('current','Current Account'),('savings','Savings Account'),('nri','NRI Account'))
    account = models.CharField(max_length=50, choices=account_select)
    # materials_select = (('cheque','Cheque Book'),('credit','Credit Card'),('debit','Debit Card'))
    materials = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name