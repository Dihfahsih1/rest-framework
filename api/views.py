"""Api Views"""
#from django.shortcuts import render
#from django.forms.models import model_to_dict
#from django.http import JsonResponse
#import  json
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def api_home(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    