from django.urls import path, re_path, include
from . import views

#app_name = 'catalog'
urlpatterns = [
    #path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:id>', views.ProductDetailView.as_view(), name='item-detail'),
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brand/<int:id>', views.BrandDetailView.as_view(), name='brand-detail'),

]

