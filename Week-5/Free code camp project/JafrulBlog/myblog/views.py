from django.shortcuts import render
from . models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'post':posts})

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'posts':post})
