from datetime import timedelta
from django.views.generic import ListView, TemplateView

from django.utils import timezone

from .models import Post, Category, Tag


class CustomMixins:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['trending_now'] = (
            Post.objects.filter(status='active', published_date__isnull=False)
            .order_by('published_date', '-views_count')[:4]
        )

        context['categories'] = Category.objects.all()[:5]
        context['tags'] = Tag.objects.all()[:10]

        return context


class NewsHomePageView(CustomMixins, ListView):
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

        week_ago = timezone.now() - timedelta(days=7)

        context['weekly_top_posts'] = (
            Post.objects.filter(
                status='active', published_date__isnull=False, published_date__gte=week_ago)
            .order_by('-published_date', '-views_count')[:7]
        )

        context['categories'] = Category.objects.all()[:5]
        context['tags'] = Tag.objects.all()[:10]

        return context


class AboutPageView(TemplateView):
    template_name = "AZnews/about.html"


class PostListView(CustomMixins, ListView):
    model = Post
    template_name = 'AZnews/main/list/list.html'
    queryset = Post.objects.filter(
        status='active',
        published_date__isnull=False,
    )
    context_object_name = 'posts'
    paginate_by = 1


class PostByCategoryView(CustomMixins, ListView):
    model = Post
    template_name = 'AZnews/main/list/list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        query = queryset.filter(
            status='active',
            published_date__isnull=False,
            category=self.kwargs["category_id"],
        )
        return query


class PostByTagView(CustomMixins, ListView):
    model = Post
    template_name = 'AZnews/main/list/list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        query = queryset.filter(
            status='active',
            published_date__isnull=False,
            tag=self.kwargs["tag_id"],
        )
        return query
