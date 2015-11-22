Title: Linux和Nvidia显卡驱动
Date: 2013-03-10 23:46
Author: algu
Category: 程序猿
Tags: 瞎折腾
Slug: linuxe5928cnvidiae698bee58da1e9a9b1e58aa8-2

由于lxde也用了将近一学期了，虽说lxde比较轻量，但显示效果实在不能说美观！又不想用GNOME或者KDE之流.它们会携带一大堆莫名其妙的软件，也受不了arch下GNOME那个样子，至于KDE,比GNOME好不了哪去.而xfce4也是直追GNOME.于是再次忍不住装上Enlightenment17,上次因为感觉e17CPU占用太多，删了.但这次为了显示效果，下决心把e17装了.跟着网上的教程算是把它配置的满意了.  
但风扇也呼呼的转了起来,top命令下去，果然，Enlightenment
CPU占用率百分之三十几，都是因为我的nvidia显卡没正常工作的缘故！而且貌似还在发热！你说你不工作去就算了，还拖累整个系统.BIOS中也没有关闭n卡的选项.无奈只有自食其力，上网搜解决方法.  

貌似官方源里有nvidia驱动，但无奈nvidia-utility和mesa-libgl冲突,而后者被我系统里的大部分软件依赖.也就不敢装它了.然后用了aur中的bumblebee软件,但在装nvidia-bumblebee时无法安装，看wiki中说bbswitch可以关闭独显，但我也没装成功,bbswitch-git倒是装
成功了，却不工作！无奈我又去nvidia官网下载驱动，倒是没有依赖问题,但装好之后，X服务器又启动不了了.把由nvidia-xconfig自动生成在/etc/X11/Xorg.conf删了之后才能启动桌面环境！可能是我没配置好什么.于是狠心去装官方源中的n卡驱动，大概把我电脑里的桌面程序都给删了，装上后X还是启动不了，于是删了X,最小安装Xorg,问题依旧，查看X日志发现错误信息中有“Intel”关键字，于是明白要装xf86-video-intel
Intel集显的开源驱动，但它依赖mesa-libgl库，于是我明白怎么回事了：这是Intel和nvidia之间的矛盾.Fuck,可却害苦了我等
草民！
