import logging

from rest_framework import serializers

log = logging.getLogger(__name__)


class EncryptSerializer(serializers.Serializer):
    given_name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=200)
    key = serializers.CharField(max_length=32)

    def validate(self, attrs):
        given_name = attrs.get('given_name')
        surname = attrs.get('surname')
        key = attrs.get('key')

        if key is not None:
            if len(key) == 32:
                pass
            else:
                msg = 'Key must bet 32 Chars'
                raise serializers.ValidationError(msg, code='invalid')
        else:
            msg = 'Must include "key".'
            raise serializers.ValidationError(msg, code='invalid')

        if given_name is not None and surname is not None:
            pass
        else:
            msg = 'Must include "given name" and "surname".'
            raise serializers.ValidationError(msg, code='invalid')

        attrs['given_name'] = given_name
        attrs['surname'] = surname
        attrs['key'] = key
        return attrs


class DecryptSerializer(serializers.Serializer):
    given_name_encrypt = serializers.CharField(max_length=100)
    surname_encrypt = serializers.CharField(max_length=200)
    key = serializers.CharField(max_length=32)

    def validate(self, attrs):
        given_name_encrypt = attrs.get('given_name_encrypt')
        surname_encrypt = attrs.get('surname_encrypt')
        key = attrs.get('key')

        if key is not None:
            if len(key) == 32:
                pass
            else:
                msg = 'Key must bet 32 Chars'
                raise serializers.ValidationError(msg, code='invalid')
        else:
            msg = 'Must include "key".'
            raise serializers.ValidationError(msg, code='invalid')

        if given_name_encrypt is not None and surname_encrypt is not None:
            pass
        else:
            msg = 'Must include "given name encrypt" and "surname encrypt".'
            raise serializers.ValidationError(msg, code='invalid')

        attrs['given_name_encrypt'] = given_name_encrypt
        attrs['surname_encrypt'] = surname_encrypt
        attrs['key'] = key
        return attrs


class EncryptBase64Serializer(serializers.Serializer):
    given_name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=200)

    def validate(self, attrs):
        given_name = attrs.get('given_name')
        surname = attrs.get('surname')

        if given_name is not None and surname is not None:
            pass
        else:
            msg = 'Must include "given name" and "surname".'
            raise serializers.ValidationError(msg, code='invalid')

        attrs['given_name'] = given_name
        attrs['surname'] = surname
        return attrs


class DecryptBase64Serializer(serializers.Serializer):
    given_name_encrypt = serializers.CharField(max_length=100)
    surname_encrypt = serializers.CharField(max_length=200)

    def validate(self, attrs):
        given_name_encrypt = attrs.get('given_name_encrypt')
        surname_encrypt = attrs.get('surname_encrypt')

        if given_name_encrypt is not None and surname_encrypt is not None:
            pass
        else:
            msg = 'Must include "given name encrypt" and "surname encrypt".'
            raise serializers.ValidationError(msg, code='invalid')

        attrs['given_name_encrypt'] = given_name_encrypt
        attrs['surname_encrypt'] = surname_encrypt
        return attrs
