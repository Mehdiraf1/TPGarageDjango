from rest_framework import permissions


class IsReceptionnist(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_receptionnist


class IsMecanic(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_mecanic)
        return request.user.is_mecanic


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_client


class IsMecanicCanChangeState(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['PUT', 'PATCH'] and list(request.data.keys()) == ['etat']


class IsCarReceptor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.receptionauthor == request.user


