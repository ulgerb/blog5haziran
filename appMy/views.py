from django.shortcuts import render, redirect
from appMy.models import *
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages # kullanıcıya mesaj gönder

# Create your views here.

def indexPage(request):
   # blogs = Comment.objects.values("blog__title").annotate(comments = Count('blog'))
   # print(blogs)
   
   blog_list = Blog.objects.all().order_by('-id')
   
   # Sidenav Start
   blog_likes = Blog.objects.annotate(q_count=Count('likes')).order_by('-q_count')
   blog_random_list = Blog.objects.all().order_by('?')
   blog_comments = Blog.objects.all().order_by('-comment_num')
   # Sidenav End
   
   context = {
      "blog_list":blog_list,
      "blog_likes":blog_likes[:5],
      "blog_random_list":blog_random_list[:4],
      "blog_comments":blog_comments[:4],
   }
   return render(request, 'index.html',context)

def detailPage(request, bid):
   blog = Blog.objects.get(id=bid)
   comment_list = Comment.objects.filter(blog=blog)
   
   if request.method == "POST":
      text = request.POST.get("text")
      # request.user => girişli kullanıcı
      comment = Comment(text=text, blog=blog, user=request.user)
      comment.save()
      
      blog.comment_num += 1
      blog.save()
      
   context = {
      "blog":blog,
      "comment_list":comment_list,
      # Sidenav Start
      "blog_likes" : Blog.objects.annotate(q_count=Count('likes')).order_by('-q_count')[:5],
      "blog_random_list" : Blog.objects.all().order_by('?')[:4],
      "blog_comments" : Blog.objects.all().order_by('-comment_num')[:4],
      # Sidenav End
   }
   return render(request, "detail.html", context)

 
def contactPage(request):

   if request.method == "POST":
      fullname = request.POST.get("fullname")
      email = request.POST.get("email")
      subject = request.POST.get("subject")
      text = request.POST.get("text")
      
      contact = Contact(fullname=fullname, email=email, title=subject, text=text)
      contact.save()
   
   context = {}
   return render( request, "contact.html", context)

def allBlogPage(request, cslug=None):
   
   if cslug:
      blog_list = Blog.objects.filter(category__slug = cslug).order_by('-id')
   else:
      blog_list = Blog.objects.all().order_by('-id')

   query = request.GET.get("query")
   if query:
      blog_list = Blog.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)) 
      
   category_list = Category.objects.all()
   
   context = {
      "blog_list":blog_list,
      "category_list":category_list,
   }
   return render( request, "blog-all.html", context)

# USER VIEWS

def loginPage(request):

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      user = authenticate(username=username, password=password) 
      # kontrol eder doğruysa kullanıcı adını yanlışsa None döndürür
      if user:
         login(request, user)
         
         return redirect("indexPage")
      else:
         messages.error(request, "Kullanıcı adı veya şifre yanlış!!")
         # [] messages listedir for ile döndürülmeli
   
   context = {}
   return render(request, 'user/login.html', context)

