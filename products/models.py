from django.db import models


# Create your models here.


class Product(models.Model):
	product_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
