from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from products.serializers import MyTokenObtainPairSerializer, ProductSerializer
from products.models import Product


class ProductViewSet(ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	# IsAdminUser : admin인 경우(is_staff : true)에만 볼 수 있음
	# IsAuthenticated : jwt access token이 있어야 볼 수 있음
	# IsAuthenticatedOrReadOnly : 권한 없는 사용자의 경우 요청 방법이 안전한 get, head, options 만 읽기만 가능, 권한이 있는 경우 쓰기 권한을 허용
	permission_classes = [IsAdminUser]


class MyObtainTokenPairView(TokenObtainPairView):
	permission_classes = (AllowAny,)
	serializer_class = MyTokenObtainPairSerializer
