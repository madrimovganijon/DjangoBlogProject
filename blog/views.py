from django.shortcuts import render, redirect
from django.forms import modelform_factory

from .models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', context={'posts':posts})

NewPostForm = modelform_factory(BlogPost, exclude=[])

def newpost(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewPostForm()
    return render(request,'blog/newpost.html', context={'form':form})