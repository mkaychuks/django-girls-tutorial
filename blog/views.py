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


# handles crating a new Form
def post_new(request):
    if request.method == 'POST': # checks the http method
        form = PostForm(request.POST)
        if form.is_valid(): # checks for all fields to be filled correctly
            post = form.save(commit=False) # creates the form but doesn't save immediately
            post.author = request.user # assigns the author to the current looged-in user
            post.published_date = timezone.now() # utilizes the publish method in the Model(Post)
            post.save() # finally saves the data sent across
            return redirect('post_detail', pk=post.pk) # redirects to the post detail...
    else:
        form = PostForm()
    context = {'form': form}
    template_name = 'blog/post_new.html'
    return render(request, template_name, context)