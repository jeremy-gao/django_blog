# django blog  
这是一个轻量级使用django 1.8.7 和python2.7.1 开发的blog系统

优点：<br>
    界面美观简洁，采用HTML5+CSS3 开发
  
缺点：<br>
    暂时还未完全开发完毕

Install:<br>
	1.首先你应该具备django运行环境，请自行安装<br>
	2.安装mysql建议mysql版本5.6(不要忘记python-MySQLdb)<br>
	3.安装相关框架：<br>
	$pip install -r requirements.txt<br>
	4.搜集静态文件到 settings.STATIC_ROOT 文件夹:<br>
	$ python manage.py collectstatic