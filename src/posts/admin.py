from django.contrib import admin

from posts.models import Category, Post

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'publication_date', 'summary', 'user')
    list_filter = ('user', 'category', 'publication_date', 'body')
    search_fields = ('title', 'summary', 'body')

