# Generated by Django 4.2 on 2023-12-15 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0006_blog_comment_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Konu')),
                ('text', models.TextField(verbose_name='Mesaj')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('fullname', models.CharField(max_length=50, verbose_name='Ad - Soyad')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user2', to=settings.AUTH_USER_MODEL, verbose_name='Beğenen Kullanıcılar'),
        ),
    ]
