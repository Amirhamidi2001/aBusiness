from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'counted_views', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    #ordering = ('-created_date',)
    search_fields = ('title', 'content')
    

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved')
    list_filter = ('post', 'approved')
    search_fields = ('name', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
