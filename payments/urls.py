from django.urls import path
from .views import PaymentInfoView

urlpatterns = [
    path("payment_info/", PaymentInfoView.as_view()),
]