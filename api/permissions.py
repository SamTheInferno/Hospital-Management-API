from rest_framework.permissions import BasePermission

class IsOfficer(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('api.add_patient')
