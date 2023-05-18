from django.views.generic import ListView

from .models import Post


class NewsHomePageView(ListView):
    model = Post
    template_name = "AZnews/home.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['trending_post'] = (
            Post.objects.filter(status='active', published_date__isnull=False)
            .order_by('-views_count')
            .first()
        )
        context['trending_posts'] = (
            Post.objects.filter(status='active', published_date__isnull=False)
            .order_by('-views_count')[1:4]
        )
        context['trending_now'] = (
            Post.objects.filter(status='active', published_date__isnull=False)
            .order_by('published_date', '-views_count')[:4]
        )
        return context
