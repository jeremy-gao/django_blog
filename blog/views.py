#encoding:utf-8
from django.shortcuts import render,get_object_or_404
from blog.models import Post,Links,Category
from blog.app import app,img
from django.db.models import Q
from blog.form import ContactForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.cache import cache_page
from django.conf import settings
# Create your views here.

@cache_page(60 * 15)
def index(request,page=1,cid=0):
	cid = int(cid);
	links = Links.objects.all();
	categories = Category.objects.all();
	if cid > 0:
		posts = Post.objects.filter(cid=cid);
	else:
		posts = Post.objects.order_by('-published_date');
	posts,page_range = app.blog_page(posts,page=page);
	posts_recent = Post.objects.order_by('-published_date')[:5];
	site_url = settings.SITE_URL;
	dict = {'posts':posts,'page_range':page_range,'links':links,'categories':categories,'cid':cid,'posts_recent':posts_recent,'site_url':site_url};
	return render(request,'blog/index.html',dict);

@cache_page(60 * 30)
def post_detail(request,id):
	post = get_object_or_404(Post, id = id);
	posts_recent = Post.objects.order_by('-published_date')[:5];
	links = Links.objects.all();
	categories = Category.objects.all();
	site_url = settings.SITE_URL;
	return render(request,'blog/single.html',{'post':post,'posts_recent':posts_recent,'categories':categories,'links':links,'site_url':site_url});

def about(request):
	return render(request,'blog/about.html',{});

global code
code=None
def contact(request,**kwargs):
	global code;
	if request.method == 'POST':
		if request.POST:
			form = ContactForm(request.POST);
			if form.is_valid() and code.lower() == str(form.img_code()).strip().lower():
				form.save();
				return HttpResponseRedirect('/index.html');
			else:
				return HttpResponse("<p>验证码不正确!</p>");
	else:
		form = ContactForm(auto_id=False);
		code = img.Code();
		img.Img(code);
		return render(request,'blog/contact.html',{'form':form});

def search(request):
	links = Links.objects.all();
	categories = Category.objects.all();
	posts_recent = Post.objects.order_by('-published_date')[:5];
	if request.GET:
		keywords = request.GET['keywords'].encode("utf-8");
		page = request.GET.get('page',1);
		posts = Post.objects.filter(Q(title__icontains=keywords)|Q(context__icontains=keywords)).order_by('-published_date');
		if posts:
			posts,page_range = app.blog_page(posts,page=page);
			return render(request,'blog/search.html',{'posts':posts,'page_range':page_range,'keywords':keywords,'links':links,'categories':categories,'posts_recent':posts_recent});
		else:
			posts = [];
			page_range = [1];
			return render(request,'blog/search.html',{'posts':posts,'page_range':page_range,'links':links,'categories':categories,'posts_recent':posts_recent});