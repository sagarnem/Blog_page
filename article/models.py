from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(verbose_name="Blog Titel", max_length=40)
    image = models.ImageField(upload_to='Blog-image/')
    detail = models.TextField(verbose_name="Details")
    created_at = models.DateField(auto_now_add=True)

def _str_(self):
    return self.name
