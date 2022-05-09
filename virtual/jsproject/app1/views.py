from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger
# Create your views here.


def index(request):
    return render(request, 'app1/base/index.html')

def postList(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app1/body/blog.html', {'page_obj':page_obj})