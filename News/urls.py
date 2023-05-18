from django.urls import path

from .views import NewsHomePageView

urlpatterns = [
    path('', NewsHomePageView.as_view(), name="home"),
]
