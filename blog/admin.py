from django.contrib import admin
from .models import Post
from .models import Comment


admin.site.site_header = 'Schools Services'
admin.site.site_title = 'Schools Services'
admin.site.register(Post)
admin.site.register(Comment)
