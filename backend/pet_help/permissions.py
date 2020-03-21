from rest_framework.permissions import IsAuthenticated


class PublicReadOwnerWritePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        if request.method == "GET":
            return True
        return obj.user == request.user


class OwnerReadWritePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return obj.user == request.user
