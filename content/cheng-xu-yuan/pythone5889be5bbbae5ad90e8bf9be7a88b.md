Title: python创建子进程
Date: 2012-10-24 19:50
Author: algu
Category: 程序猿
Tags: subprocess
Slug: pythone5889be5bbbae5ad90e8bf9be7a88b

在使用python的subprocess.Popen()创建的子进程死循环时，当设置shell=True时，使用subprocess.popen().kill()无法杀死子进程，然后换成

os.kill(proc.pid,
signal.SIGKILL),同样无法杀死，郁闷纠结之。在kill()后加上wait(),防止僵尸进程，同样无法结束。看来不是加不加wait()的事情。于是加了一条print
"PID:%d" %
proc.pid(),打印出子进程PID,发现问题了，打印出的进程号，和top显示的不一样，总是相差1，

RT

[![](http://jcodef.com/wp-content/uploads/2012/10/bug-300x168.png "bug")](http://jcodef.com/wp-content/uploads/2012/10/bug.png)

于是把改成os.kill(proc.pid+1,signal.SIGKILL), 成功杀死子进程。

于是很激动以为发现了python的bug，想着跟python社区发个邮件报告一下。

当我查看subprocess的官方说明时，发现原来人家早有提示啊，

> `Popen.pid`
> :   The process ID of the child process.<span
>     style="color: #ff0000;">Note that if you set the *shell* argument
>     to `True`, this is the process ID of the spawned shell.</span>
>     </p>
>     <div>
>
>     </div>
>
还是我看文档不够细心。<span
style="color: #000000;">这句话的google翻译结果是：</span>

<span
style="color: #000000;">“需要注意的是，如果你的shell参数设置为True，这是衍生shell的进程ID。”</span>

但为什么相差总是相差1呢？官方也没给出解释。

于是去掉shell=True,kill(),和os.kill(pid,signal.SIGKILL)都能工作。

最终源代码：

[![](http://jcodef.com/wp-content/uploads/2012/10/Screenshot-from-2012-10-24-195604-300x215.png "Screenshot from 2012-10-24 19:56:04")](http://jcodef.com/wp-content/uploads/2012/10/Screenshot-from-2012-10-24-195604.png)

helloworld.c测试代码：

[![](http://jcodef.com/wp-content/uploads/2012/10/Screenshot-from-2012-10-24-195532-300x122.png "Screenshot from 2012-10-24 19:55:32")](http://jcodef.com/wp-content/uploads/2012/10/Screenshot-from-2012-10-24-195532.png)

主要是因为自己看文档不够细心，同时早就应该尝试把shell=True去掉的。也不至于浪费那么长时间。
