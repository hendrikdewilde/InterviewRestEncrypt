import datetime
import logging

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from api.classes import IsAuthenticatedAndReadOnly, APIRootMetadata
from api.serializers import EncryptSerializer, DecryptSerializer, EncryptBase64Serializer, DecryptBase64Serializer
from libs.utils import string_to_base64, base64_to_string, Crypt

log = logging.getLogger(__name__)


class EncryptViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed by Admin.
    """
    permission_classes = [AllowAny]
    serializer_class = EncryptSerializer
    http_method_names = ['post', 'head', 'options']
    metadata_class = APIRootMetadata

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            given_name = serializer.validated_data['given_name']
            surname = serializer.validated_data['surname']
            key = serializer.validated_data['key']

            class_temp = Crypt()
            given_name_e = class_temp.encrypt_string(key, given_name)
            surname_e = class_temp.encrypt_string(key, surname)

            return Response({'given_name': given_name_e, 'surname': surname_e})
        else:
            return Response({'message': "invalid data"})


class DecryptViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed by Admin.
    """
    permission_classes = [AllowAny]
    serializer_class = DecryptSerializer
    http_method_names = ['post', 'head', 'options']
    metadata_class = APIRootMetadata

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            given_name_e = serializer.validated_data['given_name_encrypt']
            surname_e = serializer.validated_data['surname_encrypt']
            key = serializer.validated_data['key']

            class_temp = Crypt()
            given_name = class_temp.decrypt_string(key, given_name_e)
            surname = class_temp.decrypt_string(key, surname_e)

            return Response({'given_name': given_name, 'surname': surname })
        else:
            return Response({'message': "invalid data"})


class EncryptBase64ViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed by Admin.
    """
    permission_classes = [AllowAny]
    serializer_class = EncryptBase64Serializer
    http_method_names = ['post', 'head', 'options']
    metadata_class = APIRootMetadata

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            given_name = serializer.validated_data['given_name']
            surname = serializer.validated_data['surname']

            given_name_e = string_to_base64(given_name)
            surname_e = string_to_base64(surname)

            return Response({'given_name': given_name_e, 'surname': surname_e})
        else:
            return Response({'message': "invalid data"})


class DecryptBase64ViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed by Admin.
    """
    permission_classes = [AllowAny]
    serializer_class = DecryptBase64Serializer
    http_method_names = ['post', 'head', 'options']
    metadata_class = APIRootMetadata

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            given_name_e = serializer.validated_data['given_name_encrypt']
            surname_e = serializer.validated_data['surname_encrypt']

            given_name = base64_to_string(given_name_e)
            surname = base64_to_string(surname_e)

            return Response({'given_name': given_name, 'surname': surname })
        else:
            return Response({'message': "invalid data"})
# {
#     "given_name": "aGVuZHJpaw==",
#     "surname": "RGUgV2lsZGU="
# }
# 12345678901234567890123456789012
# {
#     "given_name": "gAAAAABf_fmWVnR_qs-2FKi621vU90wto8pQItEdffIV0Tub7nVQqyTYzaXWY3u3RMicOC-A16lqQQuKUdxLArx62y6nfXeQgw==",
#     "surname": "gAAAAABf_fmWUSd8Zc0LvSUmsRbppoKdHNP_XNM84ZME1s-O3-4OPxOGGIMD5r0meXTvdZ2BzuRSaV02n3oCCNRZovXvPyDRxA=="
# }