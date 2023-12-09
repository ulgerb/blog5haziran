from django.db import models
from django.contrib.auth.models import User 
# Create your models here.



class Blog(models.Model):
   user = models.ForeignKey(User,related_name="user1" ,verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Blog Yazısı"))
   image = models.ImageField(("Resim"), upload_to="blog")
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=False)
   likes = models.ManyToManyField(User,related_name="user2", verbose_name=("Beğenen Kullanıcılar"))
   
   def __str__(self) -> str: # admin panelinde obje ismi tanımlama
      return self.title
   