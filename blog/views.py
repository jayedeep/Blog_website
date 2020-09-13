from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
# posts=[
#     {
#         'author':"CoreyMS",
#         "title":"Blog Post 1",
#         "contest":"First post content",
#         "date_posted":"August 27, 2018"
#     },
# {
#         'author':"Jane Doe",
#         "title":"Blog Post 2",
#         "contest":"Second post content",
#         "date_posted":"August 29, 2018"
#     }
# ]

def home(request):

    context={
        'posts':Post.objects.all()
    }
    return render(request,"blog/home.html",context=context)

class PostListView(ListView):
    template_name = 'blog/home.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    template_name = 'blog/user_posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(auther=user).order_by('-date_posted')



def about(request):
    return render(request,'blog/about.html',{'title':"about"})

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.auther=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.auther=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.auther:
            return True
        return False