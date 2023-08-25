from django.db import models
from django.urls import reverse
# Create your models here.
class original(models.Model):
    trans_id=models.CharField(max_length=60)
    merchant=models.CharField(max_length=60,blank=True)
    country=models.CharField(max_length=60,blank=True)
    city=models.CharField(max_length=60,blank=True)
    amount=models.CharField(max_length=60,blank=True)
    currency=models.CharField(max_length=60)
    
    def get_url(self):
        return reverse('modify',args=[self.pk])
    def __str__(self):
        return f'{self.merchant}'

