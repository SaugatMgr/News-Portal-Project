from datetime import timedelta
from django.views.generic import ListView

from django.utils import timezone

from .models import Post, Category, Tag


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

        week_ago = timezone.now() - timedelta(days=7)

        context['weekly_top_posts'] = (
            Post.objects.filter(
                status='active', published_date__isnull=False, published_date__gte=week_ago)
            .order_by('-published_date', '-views_count')[:7]
        )
        
        context['categories'] = Category.objects.all()[:5]
        context['tags'] = Tag.objects.all()[:10]
        
        return context
