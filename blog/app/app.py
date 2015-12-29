from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
###



def blog_page(queryset,page_size=5,page=1,after_range_num=3,before_range_num=2):
	try:
		page = int(page);
		if page < 1:
			page = 1;
	except ValueError:
		page = 1;
	paginator = Paginator(queryset,page_size);
	try:
		posts = paginator.page(page);
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		posts = paginator.page(1);
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num:page + before_range_num];
	else:
		page_range = paginator.page_range[0:int(page) + before_range_num];
	return posts,page_range;
		