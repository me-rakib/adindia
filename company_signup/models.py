from operator import mod
from django.db import models

# Create your models here.
class Ads_catagory(models.Model):
    ad_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ad_name

class Advertisers(models.Model):
    company_name = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=30)
    company_email = models.CharField(max_length=50, unique=True)
    company_password = models.CharField(max_length=50)
    ad_price = models.IntegerField()
    # ad_name = models.ForeignKey(Ads_catagory, on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name
