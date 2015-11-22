Title: Ajax初级使用
Date: 2013-10-15 13:03
Author: algu
Category: 程序猿
Tags: Ajax
Slug: ajaxe5889de7baa7e4bdbfe794a8

当一个页面有多个地方需要使用Ajax与服务器通信时，应该尽量把发送Ajax封装成一个函数，在这个函数里面处理各种不同的请求．这样能适当减少代码的重复.

Ajax使用流程,
new XMLHttpRequest(),open(),send(),然后处理响应，根据响应内容判断，给予用户提示．大体就是这种流程．
