from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'context']}),
        # ("Contet", {'fields': ['context']}),
        ("Date Information", {
            'fields': ['published_date'], 
            'classes': ['collape']
            })
    ]
    list_display = ['title', 'published_date']
    list_filter = ["published_date"]

admin.site.register(Post, PostAdmin)