from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import redirect, render
from datetime import timedelta
from django.views.generic import View, ListView, DetailView, TemplateView

from django.utils import timezone

from .models import Post, Category, Tag
from .forms import ContactForm, NewsLetterForm, CommentForm
from django.contrib import messages


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


class PostListView(ListView):
    model = Post
    template_name = 'AZnews/main/list/list.html'
    queryset = Post.objects.filter(
        status='active',
        published_date__isnull=False,
    )
    context_object_name = 'posts'
    paginate_by = 1


class PostByCategoryView(ListView):
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


class PostByTagView(ListView):
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


class PostDetailView(DetailView):
    model = Post
    template_name = "AZnews/main/detail/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            status="active",
            published_date__isnull=False,
        )
        return query

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        current_obj = self.get_object()
        current_obj.views_count += 1
        current_obj.save()

        context['previous_post'] = (Post.objects.filter(
            status="active",
            published_date__isnull=False,
            id__lt=current_obj.id).order_by('-id').first()
        )

        context['next_post'] = (Post.objects.filter(
            status="active",
            published_date__isnull=False,
            id__gt=current_obj.id
        ).order_by('id').first())

        return context


class ContactPageView(View):
    template_name = "AZnews/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Your form has been submitted successfully.We will contact you soon."
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Cannot submit your query.Please make sure your form is valid."
            )
            return render(request, self.template_name, {"form": form})


class NewsLetterView(View):
    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get("x-requested-with")

        if is_ajax == "XMLHttpRequest":
            form = NewsLetterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'message': 'Successfully Subscribed to our News Letter.',
                    },
                    status=201,
                )

            else:
                return JsonResponse(
                    {
                        'success': False,
                        'message': 'Form is invalid.',
                    },
                    status=400,
                )
        return JsonResponse(
            {
                'success': False,
                'message': 'Cannot process.Must be and AJAX XMLHttpRequest.',
            },
            status=400,
        )


class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_id = request.POST['post']

        if form.is_valid():
            form.save()
            return redirect('post-detail', post_id)
        else:
            post = Post.objects.get(pk=post_id)
            return render(
                request,
                "AZnews/main/detail/detail.html",
                {"post": post,
                 "form": form},
            )


class PostSearchView(View):
    template_name = "AZnews/main/list/post_search.html"

    def get(self, request, *args, **kwargs):
        query = request.GET["query"]
        post_list = Post.objects.filter(
            (Q(title__icontains=query)) | (Q(content__icontains=query))
            & Q(status="active") & Q(published_date__isnull=False)
        ).order_by("-published_date")

        # pagination start
        page = request.GET.get("page", 1)
        paginate_by = 1
        paginator = Paginator(post_list, paginate_by)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        # pagination end
        return render(
            request,
            self.template_name,
            {
                "page_obj": posts,
                "query": query,
            }
        )
