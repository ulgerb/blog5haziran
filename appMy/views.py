from django.shortcuts import render
from appMy.models import *
# from django.db.models import Count

# Create your views here.

def indexPage(request):
   blog_list = Blog.objects.all()
   # blog_likes = Blog.objects.annotate(q_count=Count('likes')).order_by('-q_count')
   
   
   print(blog_likes)
   context = {
      "blog_list":blog_list,
   }
   return render(request, 'index.html',context)

def detailPage(request, bid):
   blog = Blog.objects.get(id=bid)
   context = {
      "blog":blog,
   }
   return render(request, "detail.html", context)
