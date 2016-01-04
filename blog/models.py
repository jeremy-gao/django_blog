from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
from django.contrib import admin
# Create your models here.


class Category(models.Model):
	category_name = models.CharField(max_length=20);

	def __unicode__(self):
		return self.category_name;


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

class Links(models.Model):
	link_title = models.CharField(max_length=40);
	link_url = models.CharField(max_length=40);

	def __unicode__(self):
		return self.link_title;
