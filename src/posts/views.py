from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from posts.models import Post


@login_required
def home(request):
    latest_posts = Post.objects.all().order_by('-published_date')
    context = { 'posts': latest_posts[:10] }
    return render(request, "home.html", context)


class MyPostsView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "my_posts.html"

    def get_queryset(self):
        queryset = super(MyPostsView, self).get_queryset()
        return queryset.filter(user=self.request.user)
