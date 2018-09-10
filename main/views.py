from django.shortcuts import render
from main.models import *
import random
from main.forms import CommentsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    blogs = []
    bloglist = Blog.objects.all().order_by('-created')
    paginator = Paginator(bloglist, 5)
    page = request.GET.get('page', 1)
    bloglist = paginator.page(page)
    for blog in bloglist:
        comment_count = blog.comment_set.all().count()
        style_id = random.randint(1, 4)
        tags = blog.tag.all()
        blogs.append({"comments": comment_count, "style": style_id, "blog": blog, "tags": tags})
    return render(request, "blogweb/index.html", {"blogs": blogs, "bloglist": bloglist})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'GET':
        form = CommentsForm(request)
        page = request.GET.get('page', 1)
    else:
        form = CommentsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            #print(cleaned_data)
            new_comment = Comment.objects.create(blog=blog, name=cleaned_data["name"], email=cleaned_data["email"], content=cleaned_data["content"])
            new_comment.save()
        return HttpResponseRedirect(reverse('detail', args=[blog_id]))
    comment_num = blog.comment_set.all().count()
    comments = blog.comment_set.all().order_by('-created')
    paginator = Paginator(comments, 4)
    comments = paginator.page(page)
    tags = blog.tag.all()
    preblog = Blog.objects.filter(id=blog_id - 1)
    nextblog = Blog.objects.filter(id=blog_id + 1)
    preblog = preblog[0] if preblog else None
    nextblog = nextblog[0] if nextblog else None
    return render(request, "blogweb/detail.html", {"blog": blog, "preblog": preblog, "nextblog": nextblog, "tags": tags, "comment_num": comment_num, "comments": comments})

def category(request):
    categorys = Category.objects.all()
    return render(request, "blogweb/category.html", {"categorys": categorys})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    blogs = category.blog_set.all().order_by('-created')
    return render(request, "blogweb/category_detail.html", {"blogs": blogs, "category": category})

def words(request):
    if request.method == 'GET':
        form = CommentsForm(request)
        page = request.GET.get('page', 1)
    else:
        form = CommentsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_word = Words.objects.create(name=cleaned_data["name"], email=cleaned_data["email"], content=cleaned_data["content"])
            new_word.save()
        return HttpResponseRedirect(reverse('words'))
    words = Words.objects.all().order_by('-created')
    words_num = words.count()
    paginator = Paginator(words, 4)
    words = paginator.page(page)
    return render(request, "blogweb/guestbook.html", {"words": words, "words_num": words_num})

def search(request):
    query = request.GET.get('s')
    page = request.GET.get('page', 1)
    results = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct().order_by('-created')
    count = results.count()
    paginator = Paginator(results, 10)
    results = paginator.page(page)
    return render(request, "blogweb/search.html", {"results": results, "query": query, "count": count})

def archives(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request, "blogweb/archives.html", {"blogs": blogs})

def profile(request):
    return render(request, "blogweb/profile.html")