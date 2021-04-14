from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from products.models import Product


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

	@classmethod
	def get_token(cls, user):
		token = super(MyTokenObtainPairSerializer, cls).get_token(user)

		# Add custom claims
		token['username'] = user.username
		return token


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'
