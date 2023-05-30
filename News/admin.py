from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Tag, Contact, NewsLetter, Comment

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(NewsLetter)
admin.site.register(Comment)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)