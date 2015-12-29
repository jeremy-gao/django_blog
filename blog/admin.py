from django.contrib import admin
from blog.models import Post,Links,Category
# Register your models here.

admin.site.register(Post);
admin.site.register(Links);
admin.site.register(Category);