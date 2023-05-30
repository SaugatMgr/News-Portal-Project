from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from News.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'views_count', 'published_date',)
    
        widgets = {
                "content": SummernoteWidget(),
            }