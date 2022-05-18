from django.urls import path
from products.views import ProductView, GetPerSellerView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<product_id>/', ProductView.as_view()),
    path('products/seller/<seller_id>/', GetPerSellerView.as_view()),
]
