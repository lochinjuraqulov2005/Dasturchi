from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Post

class PostView(ListView):
    model = Post
    template_name = 'base.html'
# Create your views here.
class DetalView(DetailView):
    model = Post
    template_name = 'post.html'
class CreatView(CreateView):
    model = Post
    template_name = 'post1.html'
    fields = ['title','author','body']
class UpdView(UpdateView):
    model = Post
    template_name = 'post2.html'
    fields = ['title','body']