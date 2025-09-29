from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    context = {'posts': posts}
    return render(request, "blog/index.html", context=context)


def about(request):
    context = {}
    return render(request, "blog/about.html", context=context)


def contact(request):
    context = {}
    return render(request, "blog/contact.html", context=context)


def post(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, "blog/post.html", context=context)
