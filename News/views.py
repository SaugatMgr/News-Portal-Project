from django.views.generic import ListView

from .models import Post

class NewsHomePageView(ListView):
    model = Post
    template_name = "AZnews/home.html"
    context_object_name = "posts"