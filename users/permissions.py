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
