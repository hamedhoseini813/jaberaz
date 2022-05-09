from curses import raw
from sqlite3 import Row
from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publish')
    list_filter = ('status','author','publish','created')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title','body')}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    list_editable = ('status',)
    list_display_link = ('author',)
    
