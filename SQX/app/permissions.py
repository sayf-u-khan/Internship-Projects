from rest_framework.permissions import BasePermission

class IsAllowedUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            allowed_users = ['sayf.kh4n@gmail.com',]
            return request.user.email in allowed_users
        else:
            return False