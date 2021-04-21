import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from iwaterapi.models import IwaterDriver, IwaterCompany, IwaterCategory, IwaterUsers, IwaterCompanyRegions, \
    IwaterAddresses, IwaterClients, IwaterOrders, IwaterStorage, IwaterRoles, IwaterReportApp, IwaterProviders, \
    IwaterPerms, IwaterLogs, IwaterLists, IwaterLinks, IwaterDcontrol, IwaterAuthApp, IwaterDimension
from .serializers import IwaterDriverSerializer, IwaterCategorySerializer, IwaterAddressesSerializer, CompanySerializer, \
    IwaterCompanyRegionsSerializer, IwaterUsersSerializer, AdresSerialize, OrdersSerialize, \
    StorageSerialize, RolesSerialize, DriverSerialize, ReportSerialize, ClientsSerialize, CategorySerialize, \
    ProvidersSerialize, PermsSerialize, LogsSerialize, ListSerialize, LinksSerialize, DcontrolSerialize, AuthSerialize, \
    DimensionSerialize, OrderStatusСhangesSerializer


class IwaterDriverView(APIView):
    def get(self, request):
        driver = IwaterDriver.objects.all()
        serializer = IwaterDriverSerializer(driver, many=True)
        return Response({"driver": serializer.data})

    def post(self, request):
        driver = request.data.get('driver')
        # Create an article from the above data
        serializer = IwaterDriverSerializer(data=driver)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({"success": "driver '{}' created successfully".format(driver_saved.title)})


class DetailCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset = IwaterCompany.objects.all()
    serializer_class = CompanySerializer


class DetailCompany(generics.ListCreateAPIView):
    queryset = IwaterCompany.objects.all()
    serializer_class = CompanySerializer


class IwaterCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IwaterCategory.objects.all()
    serializer_class = IwaterCategorySerializer


class IwaterCategoryList(generics.ListCreateAPIView):
    queryset = IwaterCategory.objects.all()
    serializer_class = IwaterCategorySerializer


class IwaterAddress(generics.ListCreateAPIView):
    queryset = IwaterAddresses.objects.all()
    serializer_class = IwaterAddressesSerializer


class IwaterCompanyRegion(generics.RetrieveUpdateDestroyAPIView):
    queryset = IwaterCompanyRegions.objects.all()
    serializer_class = IwaterCompanyRegionsSerializer


class IwaterCompanyRegion(generics.ListCreateAPIView):
    queryset = IwaterCompanyRegions.objects.all()
    serializer_class = IwaterCompanyRegionsSerializer

class OrderStatusСhanges(APIView):
    def get(self, request):
        order = IwaterDcontrol.objects.all()
        serializer = OrderStatusСhangesSerializer(order, many=True)
        return Response({"order": serializer.data})

    def post(self, request):
        order = request.data.get('order')
        serializer = OrderStatusСhangesSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
            return Response(status=200)({"success": "order '{}' created successfully".format(order_saved.title)})
        else:
            return  Response(status=400)


# class IwaterClient(generics.ListCreateAPIView):
#     queryset = IwaterClients.objects.all()
#     serializer_class = IwaterClientsSerializer
#
#
# class IwaterUsers(generics.ListCreateAPIView):
#     queryset = IwaterUsers.objects.all()
#     serializer_class = IwaterClientsSerializer

#
# class IwaterClients(generics.RetrieveUpdateDestroyAPIView):
#     queryset = IwaterClients.objects.all()
#     serializer_class = IwaterClientsSerializer

#############Вывод всех данных из всех таблиц################

class All_in_clusive(APIView):
    def get(self, request):
        obj1 = IwaterAddresses.objects.all()
        ser1 = AdresSerialize(obj1, many = True)

        obj2 = IwaterOrders.objects.all()
        ser2 = OrdersSerialize(obj2, many = True)

        obj3 = IwaterStorage.objects.all()
        ser3 = StorageSerialize(obj3, many = True)

        obj4 = IwaterRoles.objects.all()
        ser4 = RolesSerialize(obj4, many = True)

        obj5 = IwaterDriver.objects.all()
        ser5 = DriverSerialize(obj5, many = True)

        obj6 = IwaterReportApp.objects.all()
        ser6 = ReportSerialize(obj6, many = True)

        obj7 = IwaterProviders.objects.all()
        ser7 = ProvidersSerialize(obj7, many = True)

        obj8 = IwaterPerms.objects.all()
        ser8 = PermsSerialize(obj8, many = True)

        obj9 = IwaterLogs.objects.all()
        ser9 = LogsSerialize(obj9, many = True)

        obj10 = IwaterLists.objects.all()
        ser10 = ListSerialize(obj10, many = True)

        obj11 = IwaterLinks.objects.all()
        ser11 = LinksSerialize(obj11, many=True)

        # obj12 = IwaterDcontrol.objects.all()
        # ser12 = DcontrolSerialize(obj12, many=True)

        obj13 = IwaterAuthApp.objects.all()
        ser13 = AuthSerialize(obj13, many=True)

        obj14 = IwaterDimension.objects.all()
        ser14 = DimensionSerialize(obj14, many=True)

        obj15 = IwaterCategory.objects.all()
        ser15 = CategorySerialize(obj15, many=True)

        obj16 = IwaterClients.objects.all()
        ser16 = ClientsSerialize(obj16, many=True)


        return Response({'s1':ser1.data,'s2': ser2.data,'s3': ser3.data,'s4': ser4.data,'s5': ser5.data,'s6': ser6.data,'s7': ser7.data,'s8': ser8.data,'s9': ser9.data,'s10': ser10.data,'s11': ser11.data,'s13': ser13.data,'s14': ser14.data,'s15': ser15.data,'s16': ser16.data })






#, ser3.data, ser4.data, ser5.data, ser6.data, ser7.data, ser8.data, ser9.data, ser10.data, ser11.data, ser12.data, ser14.data, ser15.data, ser16.data, ser17.data


# class IwaterDriverInfo(APIView)

# @api_view(['GET'])
# def company_region(self, name):
#     queryset = IwaterCompanyRegions.objects.filter(company_id=name)
#     return JsonResponse(list(queryset), safe=False)
#     # return HttpResponse(json.simplejson.dumps(queryset), mimetype="application/json")
#     # return HttpResponse(json.dumps(list(queryset), ensure_ascii=False), content_type="application/json")
#     # return HttpResponse(list[0])


# class IwaterDriverCloseDay(APIView):
#     def post(self, request):
#         driver = request.data.get('driver')
#         # Create an article from the above data
#         serializer = IwaterDriverSerializer(data=driver)
#         if serializer.is_valid(raise_exception=True):
#             driver_saved = serializer.save()
#         return Response({"success": "driver '{}' created successfully".format(driver_saved.title)})


# class TwoModels(APIView):
#     order = IwaterCompany.objects.all()
#     serializer = DetailCompany(order, many=True)
#
#     ord = IwaterUsers.oject.all()
#     ser = IwaterUsersSerializer(ord, many = True)
#
#     for i in serializer.data:
#         br = str(i)
#         print(br)
#         inOrders = br[37:39]
#
#         for j in ser.data:
#             a = str(j)
#             b = a[20:23]
#             if b[2] == ')':
#                 b = a[20:22]
#             elif a[21] == ')':
#                 b = a [20]
#             else:
#                 b = a[20:30]
