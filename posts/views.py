from operator import pos
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
import datetime
from  django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def delete(request, id):
    context = {}
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        
        post.delete()
        return redirect('posts:list')
    else:
        context.update(post=post)
        return render(request, 'posts/confirm_delete.html', context)


def update(request, id):
    #메소드가 POST인경우
    if request.method == 'POST':
    #1-1. 사용자에게 전달받은 값으로 데이터 조회
        post = Post.objects.get(id=id)

    #1-2. 사용자에게 전달받은 값 확인
        title = request.POST['title']
        content = request.POST['content']
        created_by = request.POST['created_by']

    #1-3. 데이터수정
        post.title = title
        post.content = content
        post.created_by = created_by
        post.save()

    #1-4 응답
        return redirect('posts:detail', post.id)
    #2 메소드가 GET인경우
    #
    elif request.method == "GET":
    #2-1 사용자에게 전달받은 값으로 데이터 조회
        post = Post.objects.get(id=id)
        context = {'post': post}
    #2-2폼 응답
        return render(request, "posts/form.html", context)

    

def detail(request, id):
    #1. 사용자에게 전달받은 값으로 데이터 조회
    post = Post.objects.get(id=id)
    comment_list = Comment.objects.filter(post=post)
    context = {"post": post, 'comment_list': comment_list}
    #2. 응답
    return render(request, 'posts/detail.html', context)

# def new(request):
#     # 게시글 작성 HTML 응답
#     return render(request, 'form.html')

@login_required
def create(request):
    if request.method == 'POST':
    #1. 클라이언트에게 받은 값 변수 생성
        input_title = request.POST['title']
        input_content = request.POST['content']
        input_created_by = request.POST['created_by']
        #2. 게시글(post) 생성
        post = Post.objects.create(
            title = input_title,
            content=input_content,
            created_at=datetime.datetime.now(),
            created_by=input_created_by,
        )
        #3. 응답
        #return render(request,'form.html')
        return redirect("posts:detail", post.id)
        
    else:
        return render(request, 'posts/form.html')


def list(request):
    #1 게시글 전체조회
    post_all = Post.objects.all()
    context = {'post_all': post_all}
    #2. 게시글 전체, HTML응답
    return render(request, 'posts/list.html', context)

@login_required
def comment_create(request, id):
    post = get_object_or_404(Post, id=id)
    content = request.POST.get('content')
    Comment.objects.create(content=content, post=post)
    return redirect('posts:detail', post.id)
