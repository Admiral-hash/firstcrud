from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


from cyril_anorondu.blog.models import Post

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(Detailview):
    model = Post

