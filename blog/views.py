from django.shortcuts import render
from django.utils import timezone
from .models import post
from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import PostSerializer

class IntruderImage(viewsets.ModelViewSet):
    queryset= post.objects.all()
    serializer_class= PostSerializer

def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts' : posts})

def post_detail(request,pk):
    post1 = get_object_or_404(post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post1})

def post_new(request):
    form = PostForm() 
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method== "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post2 = form.save(commit=False)
            #post2.author= request.user
            post2.published_date= timezone.now()
            post2.save()
            return redirect('post_detail', pk=post2.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post4 = get_object_or_404(post, pk=pk)
    if request.method== "POST":
        form = PostForm(request.POST, instance=post4)
        if form.is_valid():
            post4 = form.save(commit=False)
            #post4.author= request.user
            post4.published_date= timezone.now()
            post4.save()
            return redirect('post_detail', pk=post4.pk)
    else:
        form = PostForm(instance=post4)
    return render(request, 'blog/post_edit.html', {'form': form})
# Create your views here.

