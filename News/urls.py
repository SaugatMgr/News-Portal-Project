from django.urls import path

from .views import (
    NewsHomePageView,
    AboutPageView,
    ContactPageView,
    PostListView,
    PostDetailView,
    PostByCategoryView,
    PostByTagView,
    NewsLetterView,
)

urlpatterns = [
    path('', NewsHomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('post-list/', PostListView.as_view(), name="post-list"),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post-by-category/<int:category_id>/',
         PostByCategoryView.as_view(), name="post-by-category"),
    path('post-by-tag/<int:tag_id>/',
         PostByTagView.as_view(), name="post-by-tag"),
    path('newsletter/', NewsLetterView.as_view(), name="newsletter"),
]
