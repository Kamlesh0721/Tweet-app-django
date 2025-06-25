from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'total_likes')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
