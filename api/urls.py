# from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from api import views
# from api.views_auth_token import obtain_auth_token_custom

router = routers.DefaultRouter()
router.register(r'encrypt', views.EncryptViewSet, basename='Encrypt')
router.register(r'decrypt', views.DecryptViewSet, basename='Decrypt')
router.register(r'encrypt_base64', views.EncryptBase64ViewSet, basename='EncryptBase64')
router.register(r'decrypt_base64', views.DecryptBase64ViewSet, basename='DecryptBase64')


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Standard
    # path('api-token-auth/', obtain_auth_token_custom, name='api_token_auth'),
]
