
from msilib.schema import ListView
from pdb import post_mortem
from winreg import DeleteValue
from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    odel = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteValue):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


