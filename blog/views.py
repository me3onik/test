from django.shortcuts import render
from .models import Post, Pet
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def title_detail(request, title):
    post = get_object_or_404(Post, title__iexact=title)
    return render(request, 'blog/detail_title.html', {'post': post})




