from django.shortcuts import render,get_object_or_404
from blog.models import Post,Links,Category
from blog.app import app

# Create your views here.

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
	dict = {'posts':posts,'page_range':page_range,'links':links,'categories':categories,'cid':cid,'posts_recent':posts_recent};
	return render(request,'blog/index.html',dict);

def post_detail(request,id):
	post = get_object_or_404(Post, id = id);
	posts_recent = Post.objects.order_by('-published_date')[:5];
	links = Links.objects.all();
	categories = Category.objects.all();
	return render(request,'blog/single.html',{'post':post,'posts_recent':posts_recent,'categories':categories,'links':links});

def about(request):
	return render(request,'blog/about.html',{});

def contact(request):
	return render(request,'blog/contact.html',{});

def search(request):
	links = Links.objects.all();
	categories = Category.objects.all();
	posts_recent = Post.objects.order_by('-published_date')[:5];
	if request.GET:
		keywords = str(request.GET['keywords'].encode("utf-8"));
		page = request.GET.get('page',1);
		posts = Post.objects.filter(title__icontains=keywords).order_by('-published_date');
		if posts:
			posts,page_range = app.blog_page(posts,page=page);
			return render(request,'blog/search.html',{'posts':posts,'page_range':page_range,'keywords':keywords,'links':links,'categories':categories,'posts_recent':posts_recent});
		else:
			posts = [];
			page_range = [1];
			return render(request,'blog/search.html',{'posts':posts,'page_range':page_range,'links':links,'categories':categories,'posts_recent':posts_recent});