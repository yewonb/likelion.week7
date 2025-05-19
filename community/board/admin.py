from django.contrib import admin
from .models import Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
  readonly_fields=('created_at',)

class CommentAdmin(admin.ModelAdmin):
  readonly_fields=('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)