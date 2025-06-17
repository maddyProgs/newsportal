from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, is_published=True)
    return render(request, 'blog/category_posts.html', {'posts': posts, 'category': category})
