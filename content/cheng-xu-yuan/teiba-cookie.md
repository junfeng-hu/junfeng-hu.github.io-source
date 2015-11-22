Title: Teiba Cookie
Date: 2013-10-28 14:00
Author: algu
Category: 程序猿
Tags: signalltiebas
Slug: teiba-cookie

首先访问<http://tieba.baidu.com/>,登陆要勾选记住我的登陆状态(即自动登录),这样Cookie才能长期有效.

对于Chrome浏览器:

右键审查元素,打开开发者工具,选择Network,刷新贴吧首页.然后上滑找到tieba.baidu.com那一项,点击headers,在Request
Headers中找到Cookie那一项,很长的一串字符串.复制到<http://signalltiebas.duapp.com/settings>页面中的Cookie框中提交就可以了.

其它浏览器类似.
