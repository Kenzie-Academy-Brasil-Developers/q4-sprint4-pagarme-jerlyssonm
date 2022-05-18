from rest_framework.permissions import BasePermission
from rest_framework.views import Request
from users.models import Users


class IsAdmin(BasePermission):

    def has_permission(self, request: Request, _):
        restricted_methods = ("GET", "PUT", "PATCH", "DELETE")
        user: Users = request.user

        if request.method in restricted_methods and user.is_anonymous:
            return False

        if request.method in restricted_methods and not user.is_admin:
            return False

        return True

class OnlyAdmAccess(BasePermission):
    def has_permission(self, request: Request, _):
        user: Users = request.user

        if user.is_anonymous:
            return False
        if not user.is_admin:
            return False
        return True

class OnlySellerAccess(BasePermission):
    def has_permission(self, request: Request, _):
        restricted_methods = ("POST", "PUT", "PATCH", "DELETE")
        user: Users = request.user

        if not request.method in restricted_methods and user.is_anonymous:
            return False

        if not user.is_seller:
            return False

        return True

class CustomerAccess(BasePermission):
    def has_permission(self, request: Request, _):
        user: Users = request.user

        if user.is_anonymous:
            return False

        return True