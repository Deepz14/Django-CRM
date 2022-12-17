from rest_framework.permissions import BasePermission


class AdminUserOnlyAction(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.admin:
            return True
        return False
