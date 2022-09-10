from django.shortcuts import render

from django.forms.models import model_to_dict
from django.http import JsonResponse
import  json
from products.models import Product
def api_home(request, *args, **kwargs):
  model_data = Product.objects.order_by("?").first()
  data={}
  if model_data:
    data=model_to_dict(model_data, fields={'id','title','price'})
    # data['Product ID']=model_data.id
    # data['title']=model_data.title
    # data['content']=model_data.content
    # data['price']=model_data.price
       
  return JsonResponse(data)
  