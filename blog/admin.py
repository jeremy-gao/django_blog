from django.contrib import admin
from blog.models import Post,Links,Category,Contact
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','published_date');
	search_fields = ('title','context');

class ContactAdmin(admin.ModelAdmin):
	list_display=('name','email','phone','message');

admin.site.register(Post,PostAdmin);
admin.site.register(Links);
admin.site.register(Category);
admin.site.register(Contact,ContactAdmin);