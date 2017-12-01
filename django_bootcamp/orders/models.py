from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Order(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return "Order ID: {0}".format(self.id)