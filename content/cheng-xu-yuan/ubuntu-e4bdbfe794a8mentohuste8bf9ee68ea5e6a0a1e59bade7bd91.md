Title: ubuntu 使用mentohust连接校园网
Date: 2012-10-31 18:52
Author: algu
Category: 程序猿
Tags: mentohust, ubuntu
Slug: ubuntu-e4bdbfe794a8mentohuste8bf9ee68ea5e6a0a1e59bade7bd91

环境：XDU+Y470+分到静态IP

**题外话**

突然间收到了静态IP，windows已无法联网，只好立即装linux，先装的DebianAMD64，启动时出现花屏，以为是版本的问题，重装成i386，依旧花屏，使用mentohust，成功联网，但显卡驱动没装好，显示影响基本浏览，然后nvidia官网下载闭源驱动，总是提示gcc版本不匹配，装成它要求的版本还是不成功。无奈换成ubuntuAMD64，显示正常，也连上了网，但重启后，又是无法联网。于是再换DebianAMD64，依旧花屏，且汉字显示为块状，......又换回ubuntu。

**正文**

首先下载mentohust（见附件）

sudo tar zxf mentohust.tar.gz -C / 解压到根目录。

cd /mentohust 进入mentohust目录

chmod a+x install 加入可执行权限

sudo ./install 安装

sudo gedit /etc/mentohust.conf

填入用户名 密码

dns设置为114.114.114.114 保存

为网卡配置静态IP地址

编辑文件/etc/network/interfaces:

sudo gdeit /etc/network/interfaces

并用下面的行来替换有关eth0的行:

\# The primary network interface

auto eth0

iface eth0 inet static

address IP地址

gateway 网关

netmask 子网掩码

dns-nameservers 114.114.114.114

保持和/etc/mentohust.conf 一致

sudo /etc/init.d/networking restart 重启网络使配置生效。

尽量不要在/etc/resolv.conf设置dns，每次重启后该文件都会被重置。

然后 sudo mentohust，

出现：

认证成功!

发送心跳包以保持在线...

欢迎来到linux世界。

参考资料：[linux连接校园网](http://xdlinux.info/wiki/index.php/Linux%E8%BF%9E%E6%8E%A5%E6%A0%A1%E5%9B%AD%E7%BD%91)

 

附件：[mentohust.tar.gz](http://pan.baidu.com/share/link?shareid=114284&uk=2887257007)
