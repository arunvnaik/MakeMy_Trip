from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user and request.user.is_staff:
            return True
        
        # Check if the request method is safe (GET, HEAD, OPTIONS)
        return request.method in SAFE_METHODS
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user and request.user.is_staff