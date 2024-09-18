from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_time_modified', 'date_time_created')
    ordering = ('status', )


admin.site.register(Post, PostAdmin)
