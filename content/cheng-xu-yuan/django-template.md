Title: Django Template
Date: 2012-09-27 18:48
Author: algu
Category: 程序猿
Tags: Django_Template
Slug: django-template

跟着《The\_Django\_Book》敲代码，在第四章创建模版对象的时候遇到了问题，
我按着书上的代码，敲了一遍又一遍，还是出错

出错信息提示环境变量未设置，然后赶紧把/site-packages/django加入环境变量，
再运行，还是不对，但我记得昨天明明成功了，遂上网百度，
然后了解到昨天我是从我建立的那个项目进入的，于是试验之，

从manage.py 进入python的交互式界面，mysite/settings.py
会导入好所需程序的环境变量。然后python就不会抛出异常了

哎！引以为鉴
