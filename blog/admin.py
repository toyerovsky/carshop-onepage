from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'status', 'created_on')
    list_filter = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
