from django.urls import path

from products.views import ProductView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<product_id>/', ProductView.as_view()),
]
