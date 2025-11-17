from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('create/', views.product_create_view, name='Product_create'),
    path('list/', views.product_list__view, name='Product_list'),
    path('upload/', views.product_upload, name='product_upload'),
    path('download/<int:product_id>/', views.download_file, name='download_file'),
    path('delete/<int:product_id>/', views.product_delete_view, name='Product_delete'),
  
]
