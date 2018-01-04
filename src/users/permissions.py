from rest_framework.permissions import BasePermission

class UsersPermission(BasePermission):

    # Listado de usuarios: solo lo puede ver un usuario admin (y por tanto autenticado)
    # Creacion de usuarios: cualquier usuario.
    # Detalle de usuario: los admi pueden ver cualquier usuaruio, usuarios autenticados (no admin) pueden ver sus datism no autenticados no puede cer nada
    # Actalizacion de usuarios: los admin pueden ver cualquier usuario, usuarrios autenticados
    # Borrado de usuario: los admin pueden ver cualquier usuario, usuarios autenticadis (noadmin) pueden ver sus datos, no autenticados no puede ver nada

    def has_permission(self, request, view):
        """
        Define si el usuario puede ejecutar una acción (GET, POST, PUT, DELETE) sobre la vista `view`
        """

        from users.api import UserDetailAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailAPI):
            return True

        if request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE"):
            return True


    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado (request.user) solo puede trabajar con el usuario solicitado (obj) si es él mismo o es un admin
        """
        return request.user == obj or request.user.is_superuser
