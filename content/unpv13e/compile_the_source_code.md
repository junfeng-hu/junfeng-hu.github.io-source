Title: 编译unpv13e源代码
Date: 2014-06-03 14:28
Author: junfeng
Category: unpv13e
Tags: unpv13e

在[这里](http://www.unpbook.com/unpv13e.tar.gz)下载源代码，根据README进行编译．

在make libfree下时需要修改inet_ntop.c, 将第60行的
`size_t size` 改成 `socklen_t size`.

貌似Linux不支持4.4BSD style routing sockets, 所以不需要编译libroute

测试intro/daytimetcpcli: `./daytimetcpcli 216.171.112.36`

而书上给的IP地址会一直block.

Then start reading the famous classic book.


