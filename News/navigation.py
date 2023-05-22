from .models import Post, Tag, Category

def navigation(request):
    trending_now=(
        Post.objects.filter(status='active', published_date__isnull=False)
        .order_by('published_date', '-views_count')[:4]
    )

    categories=Category.objects.all()[:5]
    tags=Tag.objects.all()[:10]
    
    return {
        'categories': categories,
        'tags': tags,
        'trending_now': trending_now,
    }