# from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect, get_object_or_404

from accounts.models import myUser
from .models import Blog, Comment
from django.utils import timezone
from .forms import BlogForm,BlogModelForm, CommentForm, BlogUpdate

def first(request):
    return render(request, 'first.html')

def home(request):
    #블로그 글들을 모두 띄우는 코드 db에서 블로그 글들을 모두 가져와야함
    #posts = Blog.objects.all() #블로그라는 객체를 모두 가져올거다
    posts = Blog.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts})

# blogapp 내에 templates폴더 만들고 그 안에 index.html 파일만듦

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request,'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method =='POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save() 
    return redirect('home') #함수가 잘 끝났으면 home으로 다시돌아가라

# django form을 이용해서 입력값을 받는 함수
# GET 요청과 (=입력값을 받을수있는 html을 갖다 줘야함)
# POST 요청 (=입력한 내용을 데이터베이스에 저장 즉,form에서 입력한 내용을 처리) 
# 둘다 처리가 가능한 함수
def formcreate(request):
    # 입력내용을 DB에 저장
    if request.method == 'POST':
        form = BlogForm(request.POST)
        # writer_id = request.user.id
        # writer_id = request.user
        if form.is_valid(): #입력값이 유효한지 알아서 검사해줌
            post = Blog()

            # user_id = request.session.get('user')
            # user_id = request.session.get('username')
            user_id = request.user.id
            # user = myUser.objects.get(pk = user_id)
            # post.writer = user

            post.writer = get_object_or_404(myUser, pk=user_id)

            # current_user = request.user
            # post.writer = current_user.id

            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            # post.writer = request.user.username
            post.save()
            return redirect('home')
    #입력을 받을수있는 HTML 갖다주기
    else:
        form = BlogForm()
    return render(request,'form_create.html',{'form':form})
#render의 세번째인자로 views.py내의 데이터를 html에 넘겨줄수있음
#단 딕셔너리 자료형으로 넘겨줘야함
    
def modelformcreate(request): # 이 부분만 FILES받도록 했네 
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): #입력값이 유효한지 알아서 검사해줌
            # post = Blog()
            # user = myUser.objects.get(pk = request.user.id)
            # post.writer = user
            # post.save()
            # form.writer = get_object_or_404(myUser, pk=request.user.id)
            form.save()
            return redirect('home')
    #입력을 받을수있는 HTML 갖다주기
    else:
        form = BlogModelForm()
    return render(request,'form_create.html',{'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 detali.html로 띄어주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    #Blog객체를 한 개를 가져올건데 pk값이 blog_id 값인 객체를 가져올것 
    comment_form = CommentForm()

    
    return render(request, 'detail.html',{'blog_detail':blog_detail,'comment_form':comment_form})

# def create_comment(request, blog_id):
#     filled_form = CommentForm(request.POST)
    
#     if filled_form.is_valid():
#         finished_form = filled_form.save(commit=False) #아직 저장하지말고 대기
#         finished_form.post = get_object_or_404(Blog, pk=blog_id)
#         # finished_form.writer = get_object_or_404(myUser, pk=request.user.id)
#         finished_form.save()
        
#     return redirect('detail', blog_id) #이런 blog_id를 prefix로 갖고있는 detail페이지로 이동하겠다

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        comment = Comment()
        comment.comment = filled_form.cleaned_data['comment']
        comment.post = get_object_or_404(Blog, pk=blog_id)
        comment.writer = get_object_or_404(myUser, pk=request.user.id)
        comment.save()

        
    return redirect('detail', blog_id) #이런 blog_id를 prefix로 갖고있는 detail페이지로 이동하겠다

def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    blog.delete()
    return redirect('home')

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.date=timezone.now()
            blog.save()
            return redirect('detail', blog_id)
    else:
        form = BlogUpdate(instance = blog)
        return render(request,'update.html', {'form':form})

def delete_comment(request, blog_id, comment_id):
    comment = Comment.objects.get(pk = comment_id)
    comment.delete()
    return redirect('detail', blog_id)

def update_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm(instance = comment)
        return render(request, 'update_comment.html', {'form':form})

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     comment = get_object_or_404(Comment, pk = comment_id)
    #     comment.comment = form.cleaned_data['comment']
    #     comment.save()
    #     return redirect('detail', blog_id)
    # return render(request,'update_comment.html', {'form':form})
    # if request.method =='POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment.comment = form.cleaned_data['comment']
    #         comment.save()
    #         return redirect('detail', blog_id)
    # else:
    #     form = CommentForm()
        # return render(request,'update_comment.html', {'form':form})