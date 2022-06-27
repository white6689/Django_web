from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import PostForm
from board.models import Post
from reply.forms import ReplyForm


def home(request):
    return render(request, 'board/create_basic.html')

# create
def create_basic(request):
    post=Post()
    post.title=request.POST.get("t_title")
    post.contents=request.POST.get("t_contents")
    post.save()
    return HttpResponse("성공")

@login_required(login_url='/user/login')
def create_form(request):
    if request.method=="GET":
        postForm=PostForm()
        return render(request, "board/create_form.html", {"postForm":postForm})
    elif request.method=="POST":
        postForm=PostForm(request.POST)
        if postForm.is_valid():
            post=postForm.save(commit=False)
            post.writer=request.user
            post.save()
            return HttpResponse("Form 성공")

# read
def readOne(request, bid):
    # 댓글들도 같이 가져와야해서, prefetch를 쓴다.
    try:
        post=Post.objects.prefetch_related('reply_set').get(Q(id=bid))
    except Post.DoesNotExist:
        post = None
    # post=Post.objects.get(Q(id=bid))
    replyForm = ReplyForm()
    return render(request, 'board/readone_basic.html', {"post":post, "replyForm":replyForm})

def read(request):
    posts=Post.objects.all().order_by('-id')
    return render(request, 'board/read_basic.html', {"posts":posts})

# update
@login_required(login_url='/user/login')
def update(request, bid):
    post=Post.objects.get(id=bid)
    if request.method=="GET":
        if request.user!=post.writer:
            return HttpResponse("사용자가 다릅니다.")
        postForm=PostForm(instance=post)
        return render(request, 'board/create_form.html', {"postForm":postForm})
    elif request.method=="POST":
        postForm=PostForm(request.POST, instance=post)
        if postForm.is_valid():
            post=postForm.save(commit=False)
            post.title=postForm.cleaned_data['title']
            post.contents=postForm.cleaned_data['contents']
            post.save()
            return redirect('/board/readOne/'+str(post.id))

@login_required(login_url='/user/login')
def delete(request, bid):
    post=Post.objects.get(id=bid)
    if request.user != post.writer:
        return HttpResponse("사용자가 다릅니다.")
    post=Post.objects.get(id=bid)
    post.delete()
    return redirect('/board/read')


