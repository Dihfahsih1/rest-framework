from django.urls import path
from . import views

urlpatterns = [
    path('', views.PoductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk/details', views.product_details, name="details")
]
