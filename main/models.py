from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('分类名字', max_length=16)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签名字', max_length=16)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField('博客标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    summary = models.CharField('概要', max_length=512, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField('评论者名字', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('评论内容', max_length=150)
    created = models.DateTimeField('评论时间', auto_now_add=True)

class Words(models.Model):  #留言板评论
    name = models.CharField('评论者名字', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('评论内容', max_length=150)
    created = models.DateTimeField('评论时间', auto_now_add=True)