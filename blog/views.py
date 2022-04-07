from multiprocessing import context
from django.shortcuts import render
from .models import Blog,BlogLike,BlogComment
from time import sleep
from threading import Thread
from .forms import BlogFormSet,CommentForm
# Create your views here.

# ==========================================use threadin =========================
# def timing():
#     i = 0
#     global stop_thread
#     while not stop_thread:
#         sleep(1)
#         i += 1
#         print(f"{i} second")

# def start():        
#     stop_thread = False
#     t = Thread(target=timing)
#     t.start()
#     s = 0
#     for n in range(0,10**7):
#         s += n
#         if n % 10**6 == 0:
#             print(f"{int(n/10**6)} million")
#     stop_thread = True
# ==========================================use threadin =========================


def BlogList(request):
    blogs = Blog.objects.all()
    print(blogs[1])
    context = {'blogs':blogs}
    return render(request, 'blogs/blog_list.html',context)


def BlogDetail(request,id):
    blog = Blog.objects.filter(id=id).first()
    likes = BlogLike.objects.filter(blog=id)
    like = BlogLike.objects.filter(blog=id).count()
    comments = BlogComment.objects.filter(blog=id)
    comment = BlogComment.objects.filter(blog=id).count()
    print(blog)
    context = {'blog':blog,
               'likes':likes,
               'like':like,
               'comments':comments,
               'comment':comment}
    return render(request, 'blogs/blog_detail.html',context)


def CreateBlog(request):
    form = BlogFormSet(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            print("ok")
            print(form.cleaned_data.get("title"))
            form = BlogFormSet()
    context = {"form":form}
    return render(request, 'create.html', context)

def Create(request):
    
    if request.method == 'post':
        form = CommentForm(request.POST or None)
        print("ok")
        if form.is_valid:
            print(form.cleaned_data.get("name"))
        
    form = CommentForm()       
    context = {"form":form}
    return render(request,"crt.html",context)