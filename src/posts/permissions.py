from rest_framework.permissions import BasePermission
import datetime

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method == "GET" or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        now = datetime.datetime.now()
        permission = False
        if request.method == "GET":
            if obj.publication_date.replace(tzinfo=None) <= now:
                permission = True
            else:
                if (obj.user == request.user) or request.user.is_superuser:
                    permission = True
        return permission