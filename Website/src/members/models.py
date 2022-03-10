from django.db import models

# Create your models here.
class Member(models.Model):
	id = models.BigAutoField(primary_key=True)
	username = models.TextField(max_length=128)
	password = models.TextField(max_length=128)
	address_1 = models.CharField(("Address"), max_length=128)
	address_2 = models.CharField(("Address Cont'd"), max_length=128, blank=True)
	city = models.CharField(("City"), max_length=64, default="")
	state = models.CharField(("State"), default="OH")
	zip_code = models.CharField(("Zip Code"), max_length=5, default="")
	profit_margin = models.DecimalField(decimal_places=2)
