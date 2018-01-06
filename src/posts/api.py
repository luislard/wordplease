from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly] # esta clase hace que la lista este abierta pero la creacion no

    def get_queryset(self):
        now = datetime.datetime.now()
        user = self.request.user
        queryset = Post.objects.all()
        if user.is_authenticated and user.is_superuser:
            return queryset.order_by('-publication_date')
        else:
            return queryset.filter(publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

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


class BlogUserListAPI(ListAPIView):

    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        # Getting all posts
        queryset = Post.objects.all()

        # Filtering acording kwargs
        username_arg = self.kwargs.get('username')
        queryset = queryset.filter(user__username=username_arg)
        search = self.request.query_params.get('search', None)
        title = self.request.query_params.get('title', None)
        body = self.request.query_params.get('body', None)

        if search != None and title == None and body == None:
            queryset = queryset.filter(Q(title__icontains=search) | Q(body__icontains=search))
        if title != None:
            queryset = queryset.filter(title__icontains=title)
        if body != None:
            queryset = queryset.filter(body__icontains=body)

        queryset = queryset.filter()
        if not (self.request.user.is_authenticated and (self.request.user.username == username_arg or self.request.user.is_superuser)):
            now = datetime.datetime.now()
            queryset = queryset.filter(publication_date__lte=now.strftime("%Y-%m-%d"))

        # Ordering
        order_by = self.request.query_params.get('order_by', None)
        available_order_by = ['title','-title','publication_date', '-publication_date']

        if order_by in available_order_by:
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by('-publication_date')

        return queryset


    serializer_class = PostListSerializer
#    permission_classes = (IsAdminUser,)

