from django.db import models

# # Create your models here.

class Stockrankings(models.Model):
    stockname = models.CharField(max_length=100, null = True)
    # brandlogo = models.ImageField()
    marketcap = models.IntegerField(null = True)
    revenue = models.IntegerField(null = True)
    grossprofit = models.IntegerField(null = True)
    operatingCashflow = models.IntegerField(null = True)
    netprofit = models.IntegerField(null = True)
    price =models.IntegerField(null = True)
    employee = models.IntegerField(null = True)
    dividendyield = models.IntegerField(null = True) 
    earningdate = models.CharField(max_length=100, null = True)
    country = models.CharField(max_length=100, null = True)



class Tenbaggers(models.Model):
    pass
#     stockname = models.CharField(max_length=100)
#     brandlogo = models.ImageField()
#     marketcap = models.CharField(max_length=100)
#     # revenue = models.CharField(max_length=100)
#     # grossprofit = models.CharField(max_length=100)
#     # operationprofit = models.CharField(max_length=100)
#     # netprofit = models.CharField(max_length=100)
#     # price = models.CharField(max_length=100)
#     # employee = models.CharField(max_length=100)
#     # dividendyield = models.CharField(max_length=100) 
#     # earningdate = models.CharField(max_length=100)
#     # country = models.CharField(max_length=100)
    
    
    
    
