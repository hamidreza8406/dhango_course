from django.shortcuts import render
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views import generic
from .models import Post
from .forms import NewPostForm
from django.urls import reverse_lazy


class post_list_view (generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_time_modified')


class post_detail_view(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class add_new_post(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/add_new_post.html'


class post_update(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/add_new_post.html'


class post_delete_view(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list_view')


# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-date_time_modified')
#     return render(request, 'blog/post_list.html', {'posts_list': posts_list})



# def post_detail_view(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# def add_new_post(request):
#     if (request.method == 'POST'):
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = NewPostForm()
#             return redirect('/')
#     else:
#         form = NewPostForm
#     return render(request, 'blog/add_new_post.html', context={'form': form})


# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'blog/add_new_post.html', context={'form': form})


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('/')
#
#     return render(request, 'blog/post_delete.html', context={'post': post})
