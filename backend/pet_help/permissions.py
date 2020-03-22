from rest_framework.permissions import IsAuthenticated, BasePermission


class PublicReadOwnerWritePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return super().has_permission(request, view)
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        if request.method == "GET":
            return True
        
        if request.user and request.user.is_authenticated:
            return obj.user == request.user
        return False


class OwnerReadWritePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return obj.user == request.user
