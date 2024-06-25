from article.form import BlogCreateForm, BlogEditForm
from django.shortcuts import render, redirect
from article.models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.

def create_data(request):
    form = BlogCreateForm
    if request.method=='POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context = {
        "form": form
    }
    return render (request, 'create.html', context)

def edit_data(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogEditForm(instance=blog)
    if request.method=='POST':
        form = BlogEditForm(request.POST, request.FILES, instance=blog )
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    context ={
        "data":blog,
        "form":form
    }
    return render(request,'edit.html',context)

def delete_data(request,id):
    blog = Blog.objects.get(id=id).delete()
    return redirect ('/') 
            

class Blog_view(ListView):
      model = Blog
      template_name = 'index.html'
      context_object_name = 'data'

class Blog_detail(DetailView):
    model= Blog
    template_name = 'blog.html'
    context_object_name = 'data'