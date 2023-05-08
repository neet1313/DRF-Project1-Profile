from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is Trying to edit their own profile."""

        # Return True for safe methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # Return true if object id matches requested user id
        return obj.id == request.user.id
