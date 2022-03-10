from django.db import models

# Create your models here.
class Quote_History(models.Model):
  id = models.BigIntegerField(primary_key=True)
  date = models.DateTimeField(auto_now_add=True)
  delivery_address_1 = models.CharField(_("Address"), max_length=128)
  delivery_address_2 = models.CharField(_("Address Cont'd"), max_length=128, blank=True)
  city = models.CharField(_("City"), max_length=64, default="")
  state = models.CharField(_("State"), default="", max_length=2)
  zip_code = models.CharField(_("Zip Code"), max_length=5, default="")
  gallons_requested = models.DecimalField(decimal_places=2, max_digits=3)
  price = models.DecimalField(decimal_places=2, max_digits=2)
