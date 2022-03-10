from django.db import models

# Create your models here.
class Quote_History(models.Model):
  pid = models.BigIntegerField(primary_key=True)
  date = models.DateTimeField(auto_now_add=True)
  delivery_address_1 = models.CharField(("Address"), max_length=128)
  delivery_address_2 = models.CharField(("Address Cont'd"), max_length=128, blank=True)
  city = models.CharField(("City"), max_length=64, default="")
  state = models.CharField(("State"), default="", max_length=2)
  zip_code = models.CharField(("Zip Code"), max_length=5, default="")
  gallons_requested = models.DecimalField(decimal_places=2, max_digits=3)
  price = models.DecimalField(decimal_places=2, max_digits=2)
