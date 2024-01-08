from rest_framework.permissions import BasePermission

class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        # Here I'm checking if user has admin privileges
        return request.user and request.user.is_staff