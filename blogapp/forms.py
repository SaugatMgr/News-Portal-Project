from django import forms
from News.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'views_count', 'published_date',)
    