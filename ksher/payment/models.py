from django.db import models

# Create your models here.
class Allproduct(models.Model):  # เป็นการสืบทอด class นะ จาก models.Model 
	product_name = models.CharField(max_length=200)
	product_price = models.CharField(max_length=200)

	def __str__(self):
		return self.product_name + ' - ' + self.product_price