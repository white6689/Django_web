from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from board.forms import PostForm
from board.models import Post


def home(request):
    return render(request, 'board/create_basic.html')

def create_basic(request):
    post=Post()
    post.title=request.POST.get("t_title")
    post.contents=request.POST.get("t_contents")
    post.save()
    return HttpResponse("성공")
def create_form(request):
    postForm = PostForm()


