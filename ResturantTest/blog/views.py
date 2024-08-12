from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import CommentForm

# Create your views here.


def blog_view(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {"blogs": page_obj}

    return render(request, "blog_list.html", context)


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    tag = Tags.objects.all().filter(blogs=blog)
    recent = Blog.objects.all().order_by("-time")[:4]
    category = Category.objects.all()
    comment = Comment.objects.all().filter(blog=blog)
    context = {
        "blog": blog,
        "tags": tag,
        "recent": recent,
        "category": category,
        "comment": comment,
    }

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]

            new_comment = Comment(
                blog=blog, name=new_name, email=new_email, message=new_message
            )
            new_comment.save()
    return render(request, "blog_detail.html", context)


def blog_tag(request, tag):
    blogs = Blog.objects.all().filter(tags__slug=tag)
    context = {
        'blogs':blogs
    }
    return render(request, "blog_list.html", context)
def blog_category(request, category):
    blogs = Blog.objects.all().filter(category__slug=category)
    context = {
        'blogs':blogs
    }
    return render(request, "blog_list.html", context)


def search(request):
    if request.method == 'GET':
        q = request.GET.get('search')
    blog = Blog.objects.all().filter(title__contains=q)
    context = {'blogs':blog}
    return render(request, "blog_list.html", context)