from re import T
from django.db import models

# # Create your models here.

class Stockrankings(models.Model):
    companyname = models.CharField(max_length=100, null=True)
    ticker = models.CharField(max_length=100, null=True)
    # brandlogo = models.ImageField(null=True)
    marketCap = models.FloatField(null=True)
    totalRevenue = models.FloatField(null=True)
    grossprofit = models.FloatField(null=True)
    operatingCashflow = models.FloatField(null=True)
    netIncomeToCommon = models.FloatField(null=True)
    price =models.FloatField(null=True)
    employee = models.IntegerField(null=True)
    dividendyield = models.FloatField(null=True) 
    sector = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=100, null=True)
    currency = models.CharField(max_length=100, null=True)
    priceToBook = models.FloatField(null=True)
    country = models.CharField(max_length=100, null=True)



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
    
    
    
    
