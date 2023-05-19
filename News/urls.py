from django.urls import path

from .views import (
    NewsHomePageView,
    PostListView,
    PostByCategoryView,
    PostByTagView,
)

urlpatterns = [
    path('', NewsHomePageView.as_view(), name="home"),
    path('post-list/', PostListView.as_view(), name="post-list"),
    path('post-by-category/<int:category_id>/',
         PostByCategoryView.as_view(), name="post-by-category"),
    path('post-by-tag/<int:tag_id>/',
         PostByTagView.as_view(), name="post-by-tag"),
]
