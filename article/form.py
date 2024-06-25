
from django import forms
from article.models import Blog

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'