from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import datetime

from posts.forms import PostForm
from posts.models import Post

class PostsView(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        now = datetime.datetime.now()
        queryset = super(PostsView, self).get_queryset()
        return queryset.filter(publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')


#@login_required
#def home(request):
#    latest_posts = Post.objects.all().order_by('-publication_date')
#    context = { 'object_list': latest_posts[:9] }
#    return render(request, "home.html", context)


class MyPostsView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "my_posts.html"

    def get_queryset(self):
        queryset = super(MyPostsView, self).get_queryset()
        return queryset.filter(user=self.request.user).order_by('-created_at')


class UserPostView(ListView):
    model = Post
    template_name = "user_posts.html"

    def get_queryset(self):
        now = datetime.datetime.now()
        queryset = super(UserPostView, self).get_queryset()
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username__iexact=username)
        return queryset.filter(user=user, publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')

    def get_context_data(self, **kwargs):
        username = self.kwargs.get("username")
        context = super().get_context_data(**kwargs)
        context['username'] = username
        return context


class UserPostDetailView(DetailView):
    model = Post
    template_name = "post.html"

    def get_queryset(self):
        now = datetime.datetime.now()
        queryset = super(UserPostDetailView, self).get_queryset()
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username__iexact=username)
        return queryset.filter(user=user, publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request,'post_form.html', {'form': form})

    def post(self, request):
        post = Post()
        post.user = request.user # asignamos a la pelicula el usuario autenticado
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse('post_detail_page', args=[post.user.username,post.pk])
            message = "Post created succesfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request,message)
        return render(request,'post_form.html', {'form': form})