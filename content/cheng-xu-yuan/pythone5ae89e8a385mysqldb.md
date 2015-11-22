Title: Python安装MySQLdb
Date: 2012-09-28 00:02
Author: algu
Category: 程序猿
Tags: MySQLdb安装
Slug: pythone5ae89e8a385mysqldb

本来装的Python2.7.3，后来因为一些原因换成了2.5.2，而在今天装MySQLdb的时候出问题了。在该<http://www.djangoproject.com/r/python-mysql/>下下载MySQLdbWindows安装包，装完之后，在Python环境下import
 MySQLdb

出错。然后上网搜，各种教程。都没解决，抱着试一下的态度，重新装了Python2.7.3，再重装MySQLdb，装的时候，识别出Python2.7，就明白弄对了。cmd-\>python
import MySQLdb 无异常抛出，成功。

看来有时更新版本是必须的，这样能节省很多麻烦。但MySQLdb竟然不能识别低版本的Python解释器，这有何尝不是一个小bug呢！
