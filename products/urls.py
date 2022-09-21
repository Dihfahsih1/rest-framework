from django.urls import path
from . import views

urlpatterns = [
    path('', views.PoductListCreateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/details', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/', views.ProductUpdateAPIView.as_view()),
]
