from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import BlogArticles

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/title.html',{'blogs':blogs})

def blog_articles(request,article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles,id=article_id)   # 捕获网页url请求不存在时的访问页面，当然可以用try...except来捕获，在except中用raise Http404()来处理
    publish = article.publish
    return render(request,"blog/content.html",{'article':article,'publish':publish})


