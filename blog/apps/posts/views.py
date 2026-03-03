from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
   

    def get_queryset(self):
        queryset = Post.objects.all()
        orden = self.request.GET.get('orden')

        if orden == 'categoria':
            queryset = queryset.order_by('categoria')
        elif orden == 'reciente':
            queryset = queryset.order_by('-fecha')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha')
        elif orden == 'titulo':
            queryset = queryset.order_by('titulo')

        return queryset



    

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()


