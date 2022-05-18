from django.urls import path
from .views import FeesView

urlpatterns = [
    path('fee/', FeesView.as_view()),
    path('fee/<fee_id>/', FeesView.as_view()),
]