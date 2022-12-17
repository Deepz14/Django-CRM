from rest_framework import permissions


class IsOwnerOrReadyOnly(permissions.BasePermission):
    # message = "You must be the owner of the object."
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.id == request.user.id
