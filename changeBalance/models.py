from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.conf import settings
#from cryptohash import sha1
from hashlib import sha1

class UserBalanceChange(models.Model):
    transaction_id = models.CharField(null=True, blank=True, max_length=100)
    user_id = models.CharField(null=True, blank=True, max_length=100)
    bill_id = models.CharField(null=True, blank=True, max_length=100)
    amount = models.DecimalField(_('amount'), default=0, max_digits=18, decimal_places=6) 
    
    signature = sha1.new('a')
    signature.update(f"{settings.SECRET_KEY}:{transaction_id}:{user_id}:{bill_id}:{amount}").encode('utf-8')
    signature.hexdigest()
