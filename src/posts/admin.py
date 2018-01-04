from django.contrib import admin

from posts.models import Category, Post

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'publication_date', 'summary', 'user')
    list_filter = ('id','user', 'category', 'publication_date')
    search_fields = ('title', 'summary', 'body')

