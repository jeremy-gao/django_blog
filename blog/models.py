#encoding:utf-8
from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
	category_name = models.CharField(max_length=20);

	def __unicode__(self):
		return self.category_name;
	class Meta:
		verbose_name = u'分类管理';
		verbose_name_plural = u'分类管理';


class Post(models.Model):
	title = models.CharField(max_length=200);
	# context = models.TextField();
	context = UEditorField(width='full',imagePath='images/');
	author = models.CharField(max_length=20);
	published_date = models.DateTimeField(default=timezone.now);
	tag = models.CharField(max_length=12);
	cid = models.ForeignKey(Category);

	def __unicode__(self):
		return self.title;

	def get_absolute_url(self):
		return "/post/{}/".format(self.id);
		
	class Meta:
		verbose_name = u'博文管理';
		verbose_name_plural = u'博文管理';

class Links(models.Model):
	link_title = models.CharField(max_length=40);
	link_url = models.CharField(max_length=40);

	def __unicode__(self):
		return self.link_title;
	class Meta:
		verbose_name = u'友情链接';
		verbose_name_plural = u'友情链接';

class Contact(models.Model):
	name = models.CharField(max_length = 20,blank=False);
	email = models.EmailField(max_length = 20,blank=False);
	phone = models.CharField(max_length = 11);
	city = models.CharField(max_length = 20);
	message = models.TextField(blank=False);

	def __unicode__(self):
		return self.name;

	class Meta():
		verbose_name = u'留言信箱';
		verbose_name_plural = u'留言信箱';
			
