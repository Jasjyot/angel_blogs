from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based view

def posts_create(request):
    return HttpResponse("<h1>create post</h1>")

#retrieve
def posts_detail(request):
    return HttpResponse("<h1>detail post</h1>")
def posts_list(request):
    return HttpResponse("<h1>list post</h1>")

def posts_update(request):
    return HttpResponse("<h1>update post</h1>")

def posts_delete(request):
    return HttpResponse("<h1>delete post</h1>")