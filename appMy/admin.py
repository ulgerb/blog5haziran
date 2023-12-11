from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

   list_display = ('title','user','date_now')
   list_filter = ('date_now',)
   search_fields = ('title','user__username', 'user__first_name')
   date_hierarchy = 'date_now'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

   list_display = ('blog', 'user','date_now')
   search_fields = ('blog__title','user__username')
   