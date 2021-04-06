from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from iwaterapi.models import IwaterDriver
from .serializers import IwaterDriverSerializer


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
