from django.shortcuts import render
from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer


class PoductListCreateAPIView(generics.ListCreateAPIView):
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

# Create your views here.

def product_details(request, pk):
  qs=Product.objects.get(id=pk)
  print(qs.json())
  context={"qs":qs}
  return render(request, "details.html", context)
