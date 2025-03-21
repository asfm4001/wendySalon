from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.

def index(request):
    context = {}
    return render(request, 'news/index.html', context)

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_post_list'
    def get_queryset(self):
        """ return all of posts """
        posts = Post.objects.order_by('-published_date')
        return posts

class DetailView(generic.DetailView):
    model = Post
    template_name = 'news/detail.html'
    # def get_queryset(self):
    #     post = Post.objects.filter(pk=pk)
    #     return super().get_queryset()