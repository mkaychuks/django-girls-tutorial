from django.shortcuts import render
from django.views import View


from .models import Post

# function to handle post_list
def post_list(request):
    context = {}
    template_name = 'blog/post_list.html'
    return render(request, template_name, context)
