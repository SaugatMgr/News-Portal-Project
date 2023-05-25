from django.contrib import admin

from .models import Post, Category, Tag, Contact, NewsLetter, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(NewsLetter)
admin.site.register(Comment)
