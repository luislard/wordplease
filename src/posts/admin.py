from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from posts.models import Category, Post
from django.db.models import Sum

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'publication_date', 'image', 'user', 'price')
    list_filter = ('id','user', 'category', ('publication_date', DateRangeFilter))
    search_fields = ('title', 'summary', 'body')
    list_per_page = 10

    def changelist_view(self, request, extra_context=None):
        response = super(PostAdmin, self).changelist_view(request, extra_context)
        filtered_queryset = response.context_data['cl'].queryset
        extra_context = extra_context or {}
        extra_context['total'] = filtered_queryset.aggregate(Sum('price'))
        return super(PostAdmin, self).changelist_view(request, extra_context=extra_context)