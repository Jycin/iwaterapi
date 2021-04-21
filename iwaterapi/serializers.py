from rest_framework import serializers

from .models import IwaterDriver, IwaterCategory, IwaterUsers, IwaterAddresses, IwaterCompany, IwaterCompanyRegions, \
    IwaterClients, IwaterAuthApp, IwaterClientsApp, IwaterDimension, IwaterDcontrol, IwaterLinks, IwaterLists, \
    IwaterLogs, IwaterPerms, IwaterProviders, IwaterReportApp, IwaterRoles, IwaterStorage, IwaterOrders
from rest_framework.renderers import JSONRenderer

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

# Изменение статуса заказа
class OrderStatusСhangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterDcontrol
        fields = ('order_id','tank','notice','coord')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterCompany
        fields = ('id', 'name', 'city', 'color')

class IwaterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterCategory
        fields = ('category_id', 'category', 'company_id', 'priority')

class IwaterUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterUsers
        fields = ('login', 'password', 'salt', 'session', 'name', 'phone', 'role', 'company_id', 'ban', 'region')

class IwaterAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterAddresses
        fields = ('client_id', 'contact', 'region', 'address', 'coords', 'full_address')

class IwaterCompanyRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterCompanyRegions
        fields = ('name', 'company_id')

# class IwaterClientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IwaterClients
#         fields = ('type', 'name', 'client_id', 'region', 'address')

###########Сериализаторы для всех баз##################

class AdresSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterAddresses
        fields = '__all__'


class AuthSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterAuthApp
        fields = '__all__'


class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterCategory
        fields = '__all__'


class ClientsSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterClients
        fields = '__all__'


class ClientsAppSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterClientsApp
        fields = '__all__'


class CompanySerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterCompany
        fields = '__all__'


class CompanyRegionsSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterCompanyRegions
        fields = '__all__'


class DimensionSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterDimension
        fields = '__all__'


class DcontrolSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterDcontrol
        fields = '__all__'

class LinksSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterLinks
        fields = '__all__'


class ListSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterLists
        fields = '__all__'


class LogsSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterLogs
        fields = '__all__'


class PermsSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterPerms
        fields = '__all__'


class ProvidersSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterProviders
        fields = '__all__'


class ReportSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterReportApp
        fields = '__all__'


class RolesSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterRoles
        fields = '__all__'


class StorageSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterStorage
        fields = '__all__'


class OrdersSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterOrders
        fields = '__all__'


class DriverSerialize(serializers.ModelSerializer):
    class Meta:
        model = IwaterDriver
        fields = '__all__'

# class IwaterDriverCloseDaySerializer(serializers.Serializer):
#     driver_id = serializers.IntegerField(blank=True, null=True)
#     number_containers = serializers.IntegerField()
#     total_money = serializers.FloatField()
#     login = serializers.CharField(max_length=32)
#     password = serializers.CharField(max_length=255)
#     salt = serializers.CharField(max_length=255)
#     notification = serializers.CharField(max_length=178)
#     session = serializers.CharField(max_length=128)
#     company = serializers.CharField(max_length=4)
#     stat = serializers.CharField(max_length=8)
#
#     def create(self, validated_data):
#         return IwaterDriver.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.login = validated_data.get('login', instance.login)
#         instance.password = validated_data.get('password', instance.password)
#         instance.salt = validated_data.get('salt', instance.salt)
#         instance.notification = validated_data.get('notification', instance.notification)
#         instance.session = validated_data.get('session', instance.session)
#         instance.company = validated_data.get('company', instance.company)
#         instance.stat = validated_data.get('stat', instance.stat)
#         instance.save()
#         return instance