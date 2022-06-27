from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from board.models import Post
from reply.forms import ReplyForm
from reply.models import Reply

@login_required(login_url='/user/login')
def create(request, bid):
    # post 밖에 없다. 왜? 어차피 게시글에다가 form을 불러올거라서
    if request.method=="POST":
        replyForm=ReplyForm(request.POST)
        if replyForm.is_valid():
            reply=replyForm.save(commit=False)
            reply.writer=request.user
            post=Post()
            post.id=bid
            reply.post=post
            reply.save()
        return redirect('/board/readOne/'+str(post.id))

@login_required(login_url='/user/login')
def delete(request, bid):
    reply=Reply.objects.get(id=bid)
    post=reply.post
    if request.user==reply.writer:
        reply.delete()
    return redirect('/board/readOne/'+str(post.id))

@login_required(login_url='/user/login')
def update(request,bid):
    reply=Reply.objects.get(id=bid)
    if request.method=="GET":
        if request.user == reply.writer:
            replyForm=ReplyForm(instance=reply)
            return render(request, 'reply/createReply.html', {"replyForm":replyForm})
    elif request.method=="POST":
        replyForm=ReplyForm(request.POST, instance=reply)
        if replyForm.is_valid():
            reply.contents=replyForm.cleaned_data['contents']
            return redirect('/reply/readReply')