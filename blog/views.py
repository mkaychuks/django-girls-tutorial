from django.shortcuts import render
from django.views import View
from django.utils import timezone

from .models import Post


# function to handle post_list
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')
    context = {
        'posts': posts
    }
    template_name = 'blog/post_list.html'
    return render(request, template_name, context)
