Title: python-tornado起步
Date: 2012-09-19 00:01
Author: algu
Category: 程序猿
Tags: python-tornado
Slug: python-tornadoe8b5b7e6ada5

今天终于在linux、windows下把python tornado web server 搭建好了

但在linux下编这个程序的时候发现通过不了（windows下可以通过）

>     import tornado.ioloop 
>
>     import tornado.web
>
>      class MainHandler(tornado.web.RequestHandler): 
>
> ``` {style="padding-left: 30px;"}
> def get(self): 
> ```
>
> ``` {style="padding-left: 60px;"}
> self.write("Hello Python-Tornado！") 
> ```
>
>     application = tornado.web.Application([ (r"/", MainHandler), ])
>
>      if __name__ == "__main__":
>
> ``` {style="padding-left: 30px;"}
>  application.listen(8888)
> ```
>
> ``` {style="padding-left: 30px;"}
> tornado.ioloop.IOLoop.instance().start()
> ```

    按照这个代码敲，提示Application类无listen方法，然后又纠结了半天，

    在网上看到了另一种写法，就改成了这样：

     linux下、windows下皆可通过！

    可能还是linux下的tornado没装好！！

    明天再研究！！
