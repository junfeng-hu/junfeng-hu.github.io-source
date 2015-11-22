Title: 完美的goagent
Date: 2013-01-28 17:30
Author: algu
Category: 程序猿
Tags: goagent
Slug: e5ae8ce7be8ee79a84goagent

给我们这些没钱买vpn又想出去的人带来了很大的方便。

chromium 设置-\>高级设置-\> 管理证书-\>授权中心-\>导入

选择 goagent/local/CA.crt

全部打勾，确定。

ssl证书不受信任得到了解决。

少部分要求证书的https也可以访问了。

而在Android手机上，安装GaeProxy软件，打开，修改代理地址改成
https://yourappid.appspot.com/fetch.py

Google+,facebook,twitter什么的，都可以访问了。
