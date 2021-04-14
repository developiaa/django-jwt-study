"""django_jwt_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
	TokenVerifyView,
)

urlpatterns = [
	path('admin/', admin.site.urls),
	# username, password을 보내고 refresh, access 토큰 재발급
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	# refresh token을 보내고 access 토큰 재발급
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	# verify > refresh token 검증
	path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
