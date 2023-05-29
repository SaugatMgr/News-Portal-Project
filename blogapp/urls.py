from django.urls import path
from .views import (
    BlogCreateView,
    BlogHomePageView,
    BlogDetailView,
    BlogUnpublishedPostsView,
    BlogUnpublishedPostsDetailView,
    BlogPublishPostView,
    BlogUpdateView,
    BlogDeleteView,
    BlogUnpublishedPostDeleteView,
)

app_name="news-admin"
urlpatterns = [
    path('', BlogHomePageView.as_view(),
         name="home"),

    path('post-create/', BlogCreateView.as_view(),
         name='create_post'),

    path('<int:pk>/post-detail/', BlogDetailView.as_view(),
         name="post_detail"),

    path('unpublished-posts/', BlogUnpublishedPostsView.as_view(),
         name="unpublished_posts"),

    path('<int:pk>/unpublished-post-detail/', BlogUnpublishedPostsDetailView.as_view(),
         name="unpublished_post_detail"),

    path('<int:pk>/post-update/', BlogUpdateView.as_view(),
         name="post_update"),
    
    path('<int:pk>/publish-post/', BlogPublishPostView.as_view(),
         name='publish_post'),

    path('<int:pk>/post-delete/', BlogDeleteView.as_view(),
         name="post_delete"),

    path('<int:pk>/unpublished-post-delete/', BlogUnpublishedPostDeleteView.as_view(),
         name="unpublished_post_delete"),
]
