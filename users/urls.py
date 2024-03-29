from django.urls import path

from users.views import LoginView, UserView

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", LoginView.as_view()),
]