"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.api import PostsListAPI, BlogListAPI, BlogUserListAPI, PostDetailAPI
from posts.views import MyPostsView, PostsView, UserPostView, UserPostDetailView, CreatePostView
from users.api import UserListAPI, UserDetailAPI
from users.views import logout, LoginView, UsersView, SignupView
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name="login_page"),
    path('logout', logout, name="logout_page"),
    path('signup', SignupView.as_view(), name="signup_page"),

    # path('posts/crear', CreateMovieView.as_view(), name="create_movie_page"),
    # path('pelis/<int:pk>', movie_detail, name="movie_detail_page"),
    path('posts/', MyPostsView.as_view(), name='my_posts_page'),
    path('', PostsView.as_view(), name="home_page"),

    path('blogs/', UsersView.as_view(), name='blogs_page'),
    path('blogs/<slug:username>', UserPostView.as_view(), name="blog_user_page"),
    path('blogs/<slug:username>/<int:pk>', UserPostDetailView.as_view(), name="post_detail_page"),
    path('new-post/', CreatePostView.as_view(), name="create_post_page"),

    # API REST
    path('api/1.0/users/', UserListAPI.as_view(), name="api_users_list"),
    path('api/1.0/blogs/', BlogListAPI.as_view(), name="api_blogs_list"),
    path('api/1.0/blogs/<slug:username>', BlogUserListAPI.as_view(), name="api_blogs_user_list"),
    path('api/1.0/users/get-token/', views.obtain_auth_token, name="api_obtain_token"),
    path('api/1.0/users/<slug:pk>', UserDetailAPI.as_view(), name="api_users_detail"),

    path('api/1.0/posts/', PostsListAPI.as_view(), name="api_users_list"),
    path('api/1.0/posts/<int:pk>', PostDetailAPI.as_view(), name="api_post_detail"),

]
