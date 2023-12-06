from django.shortcuts import render
from appMy.models import *
# Create your views here.

def indexPage(request):

   blog_list = Blog.objects.all()
   
   context = {
      "blog_list":blog_list,
   }
   return render(request, 'index.html',context)
