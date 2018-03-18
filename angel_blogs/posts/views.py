from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

#function based view

def posts_create(request):
    return HttpResponse("<h1>create post</h1>")

#retrieve
def posts_detail(request):
    instance=get_object_or_404(Post,id=1)
    #Post.objects.get(id=1)
    context={ 
        "title":instance.title,
        "instance":instance
    }
    return render(request,"posts_detail.html",context)

def posts_list(request):
    queryset=Post.objects.all()
    context={
        "object_list":queryset,
        "title":"List"
    }
    return render(request,"index.html",context)

def posts_update(request):
    return HttpResponse("<h1>update post</h1>")

def posts_delete(request):
    return HttpResponse("<h1>delete post</h1>")