Title: signal函数和sigaction函数
Date: 2013-02-16 13:43
Author: algu
Category: 程序猿
Tags: signal
Slug: signale587bde695b0e5928csigactione587bde695b0

环境:Linux version 3.6.10-1-ARCH

当使用系统自带signal函数处理信号时,系统并未把被捕捉到的信号加到信号屏蔽字中.

使用sigaction函数实现的signal函数(apue),在调用信号处理程序时,捕捉到的信号屏蔽字被加入到信号屏蔽字,处理程序返回后,恢复到原来的屏蔽字.

看来敲敲代码还是能发现一些东西的.
