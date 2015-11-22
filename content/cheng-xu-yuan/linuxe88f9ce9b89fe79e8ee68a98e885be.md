Title: Linux菜鸟瞎折腾
Date: 2012-09-20 23:37
Author: algu
Category: 程序猿
Tags: Debian安装
Slug: linuxe88f9ce9b89fe79e8ee68a98e885be

昨天在命令行下输入了aptitude
upgrade命令之后不知怎么的，linux内核竟然升级了，升级也挺好的，可关键是旧的版本也还存在。这样在开机时就出现了这种情况：  
RT  

[![](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo1.jpg "buhuo1")](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo1.jpg)

然后我就不爽了，本来一个内核就有两个选项：一个是图形界面，一个是命令行。现在又多了一个内核，也就有四个选项可以选择了。

实在是看着不舒服，也就一个小小的虚拟机，看着貌似装了四个系统！

于是就在ChinaUnix论坛询问，感谢网友们的热心回答，我知道了怎么删除那个旧内核的方法:

在终端或命令行下输入：

dpkg --get-selections|grep linux

然后在root权限下输入：

dpkg --purge --force-remove-essential linux-image-XXX

XXX为要卸载的旧的版本号

就这样，成功卸载了旧的linux内核

如图：

[![](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo2.jpg "buhuo2")](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo2.jpg)

但是前面还是有那个蓝色的画面。继续请教，得知;

grub需要升级到grub2。

我键入命令：

upgrade-from-grub-legacy

在让选择安装在哪个文件夹下的时候，我尝试了好几次，就是选不中，按enter键会提示你不装grub会怎么怎么。。。

我想装上啊，可是选不中！没办法，我只好选否！然后就悲剧了！

RT

[![](http://www.jcodef.com/wp-content/uploads/2012/09/buhou3.jpg "buhou3")](http://www.jcodef.com/wp-content/uploads/2012/09/buhou3.jpg)

没了操作系统启动程序，然后就Error了！

我又向高手提问，可能是高手嫌我水平太次了，我也感觉很后悔！要是在服务器下，我这样的话那损失就大了！！

于是我上网搜解决方法，可网上很多都是删除GRUB的方法！！我无奈，只好重装系统。最笨的一种方法！

刚开始一切顺利，因为以前也装过几次，这次选的就是图形专家模式，可在选择linux内核版本的时候，我为了最求最新版，选了一个比较新的版本，可是快装成功的时候，竟然提示该内核版本不支持我的CPU，也多次退回去重新操作，可是还是没成功！

万般无奈，再次重装，这次选的是普通模式（install），在装到选择APT源的时候，发现无法更改APT源，只能从国外的源里下载，十几K的速度，麻木的再次重启、重装。依旧是Install模式，这次选择不从网上下载软件，可是选择之后，进度条却不走了！

心理哭着再次重装、这次还是坚持第一次的选择吧！选择Advanced-\>Graphic
Advanced Install，这次选择较低的linux版本 ，设置了学校的源，安装成功！！

在安装的时候没选桌面环境，因为不想用默认的Gnome桌面管理环境。自己装了一个wmaker桌面环境，可是我水平比较菜，终端中文输出为乱码。也不知怎么解决，于是只好aptitude
install gnome，然后就装好了！弄了一下午啊

秀秀自己的桌面，还不怎么会设置，比较难看。

[![](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo4-300x229.jpg "buhuo4")](http://www.jcodef.com/wp-content/uploads/2012/09/buhuo4.jpg)

最后得到了几个教训，在Debian linux下慎用aptitude
upgrade！不知道会出现什么东东！

一定要养成做备份的习惯，关键时候会让你省很多力气的，

不然有你哭的！

当然“远离电脑，珍爱生命，没事不要瞎折腾！”是最好的了！！
