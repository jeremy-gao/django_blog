from django.contrib import admin
from blog.models import Post,Links,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','published_date');
	search_fields = ('title','context');

admin.site.register(Post,PostAdmin);
admin.site.register(Links);
admin.site.register(Category);