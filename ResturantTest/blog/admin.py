from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)

class BlogAdmin(admin.ModelAdmin):

    list_display = ('author', 'title', 'time')
    list_filter = ("author",)
    search_fields = ('title',)
    ordering = ('author','time')
    date_hierarchy = 'time'
admin.site.register(Blog, BlogAdmin)