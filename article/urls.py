
from django.urls import path
from article.views import Blog_view, create_data, edit_data, delete_data, Blog_detail

urlpatterns = [
    path('', Blog_view.as_view(), name= "Blog_page"),
    path('create', create_data, name= "create_blog"),
    path('edit/<id>', edit_data, name= "edit_blog"),
    path('delete/<id>', delete_data, name= "delete_blog"),
    path('blog/<int:pk>', Blog_detail.as_view(), name= "blog_detail"),

]
