Title: file descriptor
Date: 2013-09-07 11:39
Author: algu
Category: 程序猿
Tags: 文件描述符
Slug: file-descriptor

和文件描述符有关的函数：

-   open
-   close
-   dup
-   dup2
-   fcntl

文件描述符为int整型变量，范围0-OPEN\_MAX;

在linux下OPEN\_MAX未在limits.h下定义，使用sysconf(\_SC\_OPEN\_MAX)获得其值．

open打开文件返回文件描述符没什么好说的．

close()关闭文件描述符，注意当有多个文件描述符指向同一文件表项时，必须close所有与之关联的描述符才能真正关闭文件．

> When all file descriptors associated with an open file description
> have been closed, the open file  description shall be freed.

此时无法再对文件进行更改．

dup(),dup2()复制现存的文件描述符，在内核数据中一个新的文件描述符被创建．当总数达到OPEN\_MAX时，进程无法再打开文件．

当cmd=F\_DUPFD时 fcntl和dup,dup2功能类似．

附测试程序：

\#include\<unistd.h\>  
\#include\<stdio.h\>  
\#include\<limits.h\>  
\#include\<fcntl.h\>  
\#include\<errno.h\>  
int main()  
{  
int i,f,open\_max;  
open\_max=sysconf(\_SC\_OPEN\_MAX);  
for (i=3;i\<open\_max;++i)  
dup(STDOUT\_FILENO);  
// close(open\_max-1);  
f=open("test",O\_WRONLY|O\_CREAT,S\_IRUSR|S\_IWUSR);  
if (errno==EMFILE)  
printf("ERROR\\n");  
else  
printf("%d\\n",f);  
return 0;

}
