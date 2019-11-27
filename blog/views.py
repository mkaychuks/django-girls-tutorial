from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone

from .models import Post
from .forms import PostForm


# function to handle post_list
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date') # first filters the posts using the negative published_date
                                 # and then orders it accordingly...
    context = {
        'posts': posts
    }
    template_name = 'blog/post_list.html'
    return render(request, template_name, context)


# handles the post detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # gets a specific post using the PrimaryKey
    context = {
        'post': post
    }
    template_name = 'blog/post_detail.html'
    return render(request, template_name, context)
