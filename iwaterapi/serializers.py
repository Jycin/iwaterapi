from rest_framework import serializers

from .models import IwaterDriver


class IwaterDriverSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=255)
    salt = serializers.CharField(max_length=255)
    notification = serializers.CharField(max_length=178)
    session = serializers.CharField(max_length=128)
    company = serializers.CharField(max_length=4)
    stat = serializers.CharField(max_length=8)

    def create(self, validated_data):
        return IwaterDriver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.salt = validated_data.get('salt', instance.salt)
        instance.notification = validated_data.get('notification', instance.notification)
        instance.session = validated_data.get('session', instance.session)
        instance.company = validated_data.get('company', instance.company)
        instance.stat = validated_data.get('stat', instance.stat)
        instance.save()
        return instance