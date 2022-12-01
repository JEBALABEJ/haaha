from django.shortcuts import render
from blog.models import Post

# Create your views here.

def langing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',   #templates 아래에 있는 single_pages/landing.html(view가 연결해줄 템플릿 이름)
                  {'recent_posts' : recent_posts})

def about_me(request):
    return render(request, 'single_pages/about_me.html')