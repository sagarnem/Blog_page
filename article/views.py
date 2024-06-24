from django.shortcuts import render
from article.models import Blog

# Create your views here.

def featch_data(request):
    a = Blog.objects.all()

    context={
        "data": a
    }

    return render (request, 'index.html', context)