from django.shortcuts import render
from .models import Post, Pet
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def author_detail(request, author):
    obj = get_object_or_404(Post, author__iexact=author)
    return render(request, 'blog/detail_author.html', {'obj': obj})




