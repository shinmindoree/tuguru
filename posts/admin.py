from django.contrib import admin
from .models import Post, Comment

# # Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'title', 'is_view', 'created_at']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'created_by', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass