from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer
import datetime

from users.permissions import UsersPermission
from users.serializers import BlogListSerializer


class PostsListAPI(ListCreateAPIView):

    #queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly] # esta clase hace que la lista este abierta pero la creacion no

    def get_queryset(self):
        now = datetime.datetime.now()
        user = self.request.user
        #queryset = super(PostsListAPI, self).get_queryset()
        queryset = Post.objects.all()
        if user.is_authenticated and user.is_superuser:
            return queryset.order_by('-publication_date')
        else:
            return queryset.filter(publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

    # documentacion en http://www.django-rest-framework.org/api-guide/generic-views/
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    # documentacion en http://www.django-rest-framework.org/api-guide/generic-views/
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class BlogListAPI(APIView):

    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [UsersPermission]

    def get(self, request):
        users = User.objects.all()
        query_params = request.query_params
        blog_name = query_params.get('blog_name', None)
        if blog_name is not None:
            users = users.filter(username__icontains=blog_name)
        order = query_params.get('order', 'ASC')
        if (order is not 'ASC') and order == 'DESC':
            users = users.order_by('-username')
        else:
            users = users.order_by('username')
        # agregamos el paginador
        paginator = PageNumberPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        # tenemos que devolver en el response datos primitivos integers, floats, booleans, tuples, lists, dictionaries, strings
        serializer = BlogListSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)


class BlogUserListAPI(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [UsersPermission]

    def get(self, request):
        users = User.objects.all()
        paginator = PageNumberPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = BlogListSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)