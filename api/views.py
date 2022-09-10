from django.shortcuts import render

from django.forms.models import model_to_dict
#from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import  json
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
  instance = Product.objects.order_by("?").first()
  data={}
  if instance:
    data=model_to_dict(instance, fields={'id','title','price'}) #specifiy the fields to retrieve
    #data=model_to_dict(model_data)#get all fields
    data=ProductSerializer(instance).data
  return Response(data)
  