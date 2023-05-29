from typing import Any, Dict
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from News.models import Post
from .forms import PostForm


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('news-admin:unpublished_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogHomePageView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'published_posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False).order_by('-published_date')


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_queryset(self):
        queryset = Post.objects.filter(
            pk=self.kwargs['pk'], published_date__isnull=False)
        return queryset


class BlogUnpublishedPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/unpublished_posts.html'
    context_object_name = 'unpublished_posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)


class BlogUnpublishedPostsDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/unpublished_post_detail.html'
    context_object_name = 'unpublished_post'
    
    def get_queryset(self):
        queryset = Post.objects.filter(
            pk=self.kwargs['pk'], published_date__isnull=True)
        return queryset


class BlogPublishPostView(View):
    def get(self, request, pk, *args, **kwargs):
        unpublished_post = Post.objects.get(pk=pk, published_date__isnull=True)
        unpublished_post.published_date = timezone.now()
        unpublished_post.save()
        return redirect('news-admin:post_detail', unpublished_post.pk)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = (
        'title',
        'content',
        'featured_image',
        'status',
        'category',
        'tag',
    )
   
    def test_func(self):
        current_user = self.get_object()
        return current_user.author == self.request.user

    def get_success_url(self):
        current_post = self.get_object()

        if current_post.published_date:
            return reverse_lazy('news-admin:post_detail', kwargs={'pk': current_post.pk})
        else:
            return reverse_lazy('news-admin:unpublished_post_detail', kwargs={'pk': current_post.pk})


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('news-admin:home')

    def test_func(self):
        current_user = self.get_object()
        return current_user.author == self.request.user


class BlogUnpublishedPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/unpublished_post_delete.html'
    success_url = reverse_lazy('news-admin:unpublished_posts')

    def test_func(self):
        current_user = self.get_object()
        return current_user.author == self.request.user
