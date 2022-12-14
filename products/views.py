from django.shortcuts import render
from rest_framework import generics,mixins 

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissions



class PoductListCreateAPIView(StaffEditorPermissions,
                              generics.ListCreateAPIView,):
  """Use authentication token to authorize access to the API"""
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  
  def perform_create(self, serializer):
    print(serializer)
    serializer.save()
    title=serializer.validated_data.get('title')
    content=serializer.validated_data.get('content') or None
    
    if content is None:
      content=title
    serializer.save(content=content)
    
class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer

class ProductDestroyAPIView(StaffEditorPermissions,
                            generics.DestroyAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  lookup_field = 'pk'
  
  def perform_destroy(self, instance):
    super().perform_destroy(instance)
  
class ProductUpdateAPIView(StaffEditorPermissions, 
                           generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content=instance.title
 
def product_details(request, pk):
  qs=Product.objects.get(id=pk)
  print(qs.json())
  context={"qs":qs}
  return render(request, "details.html", context)


"""The above CRUD can be implemented using MIXINS in a single class"""

class ProductMixinView(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  generics.GenericAPIView
  ):
  queryset =Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  def get(self, request, *args, **kwargs):
    pk = kwargs.get("pk")
    print(pk)
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)
    
  def post(self,request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

